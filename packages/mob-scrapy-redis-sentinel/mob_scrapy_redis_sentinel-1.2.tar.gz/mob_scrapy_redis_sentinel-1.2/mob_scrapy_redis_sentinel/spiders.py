# -*- coding: utf-8 -*-
import time

try:
    from collections import Iterable
except:
    from collections.abc import Iterable

from scrapy import signals
from scrapy.exceptions import DontCloseSpider
from scrapy.spiders import Spider, CrawlSpider

from . import connection, defaults
from .utils import bytes_to_str

import json
from mob_scrapy_redis_sentinel.utils import make_md5
from mob_scrapy_redis_sentinel import inner_ip

import requests
import base64
import traceback
from mob_tools.mobLog import MobLoguru

mob_log = MobLoguru()


class RedisMixin(object):
    """Mixin class to implement reading urls from a redis queue."""
    queue_name = None  # mob rocket mq name
    redis_key = None
    latest_queue = None
    redis_batch_size = None
    redis_encoding = None

    # Redis client placeholder.
    server = None

    # Idle start time
    spider_idle_start_time = int(time.time())

    def start_requests(self):
        """Returns a batch of start requests from redis."""
        return self.next_requests()

    def setup_redis(self, crawler=None):
        """Setup redis connection and idle signal.

        This should be called after the spider has set its crawler object.
        """
        if self.server is not None:
            return

        if crawler is None:
            # We allow optional crawler argument to keep backwards
            # compatibility.
            # XXX: Raise a deprecation warning.
            crawler = getattr(self, "crawler", None)

        if crawler is None:
            raise ValueError("crawler is required")

        settings = crawler.settings

        if self.redis_key is None:
            self.redis_key = settings.get("REDIS_START_URLS_KEY", defaults.START_URLS_KEY)

        self.redis_key = self.redis_key % {"name": self.name}

        if settings.getbool("MQ_USED", defaults.MQ_USED):  # 使用了mq, 区分和生产队列名称
            self.redis_key = self.name
            self.queue_name = defaults.QUEUE_NAME_PREFIX.format(self.name)
            mob_log.info(f"mq queue_name: {self.queue_name}, redis_key: {self.redis_key}").tracker()

        if not self.redis_key.strip():
            raise ValueError("redis_key must not be empty")

        if self.latest_queue is None:
            self.latest_queue = settings.get("LATEST_QUEUE_KEY", defaults.LATEST_QUEUE_KEY)
        self.latest_queue = self.latest_queue % {"name": self.name}

        if self.redis_batch_size is None:
            # TODO: Deprecate this setting (REDIS_START_URLS_BATCH_SIZE).
            self.redis_batch_size = settings.getint(
                "REDIS_START_URLS_BATCH_SIZE", settings.getint("CONCURRENT_REQUESTS")
            )

        try:
            self.redis_batch_size = int(self.redis_batch_size)
        except (TypeError, ValueError):
            raise ValueError("redis_batch_size must be an integer")

        if self.redis_encoding is None:
            self.redis_encoding = settings.get("REDIS_ENCODING", defaults.REDIS_ENCODING)

        mob_log.info(f"Reading start URLs from redis {self.__dict__} ").tracker()

        self.server = connection.from_settings(crawler.settings)

        if self.settings.getbool("REDIS_START_URLS_AS_SET", defaults.START_URLS_AS_SET):
            self.fetch_data = self.server.spop
            self.count_size = self.server.scard
        elif self.settings.getbool("REDIS_START_URLS_AS_ZSET", defaults.START_URLS_AS_ZSET):
            self.fetch_data = self.pop_priority_queue
            self.count_size = self.server.zcard
        elif self.settings.getbool("MQ_USED", defaults.MQ_USED):  # 使用MQ
            self.fetch_data = self.pop_batch_mq
            self.count_size = self.get_queue_size
            # 爬虫启动时，检查队列是否存在,不存在则创建
            crawler.signals.connect(self.check_queue, signal=signals.spider_opened)
        else:
            self.fetch_data = self.pop_list_queue
            self.count_size = self.server.llen

        # 爬虫启动时，会先从备份队列，取出任务
        crawler.signals.connect(self.spider_opened_latest_pop, signal=signals.spider_opened)

        # The idle signal is called when the spider has no requests left,
        # that's when we will schedule new requests from redis queue
        crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)

    def check_queue(self):
        if not self.get_queue_size(self.queue_name):
            mob_log.warning(f"{self.queue_name} queue is not exist, now create it").tracker()
            self.create_queue(self.queue_name)

    def pop_list_queue(self, redis_key, batch_size):
        with self.server.pipeline() as pipe:
            pipe.lrange(redis_key, 0, batch_size - 1)
            pipe.ltrim(redis_key, batch_size, -1)
            datas, _ = pipe.execute()
        return datas

    def get_queue_size(self, redis_key):
        try:
            r = requests.get(defaults.GET_QUEUE_SIZE.format(queueName=self.queue_name), timeout=5)
            return int(r.json()['data']['queueSize'])
        except:
            mob_log.error(f"spider name: {self.name}, inner ip: {inner_ip}, get mq queue size error: {traceback.format_exc()}").tracker()

    def pop_batch_mq(self, redis_key, batch_size):
        datas = []
        for i in range(batch_size):
            queue_data = self.pop_mq(self.queue_name)
            if queue_data:
                datas.append(queue_data)
        return datas

    def pop_mq(self, queue_name):
        try:
            r = requests.get(defaults.POP_MESSAGE.format(queueName=queue_name), timeout=5)
            resp = r.json()
            if resp.get("error_code") == 0 and resp.get("data"):
                message = resp["data"]["message"]
                queue_data = base64.b64decode(message)
                return queue_data
        except:
            mob_log.error(f"spider name: {self.name}, inner ip: {inner_ip}, pop mq error: {traceback.format_exc()}").tracker()

    def create_queue(self, queue_name):
        try:
            r = requests.get(defaults.CREATE_QUEUE.format(queueName=queue_name), timeout=5)
            return r.json()
        except:
            mob_log.error(f"spider name: {self.name}, inner ip: {inner_ip}, create mq error: {traceback.format_exc()}").tracker()

    def send_message2mq(self, queue_name, queue_data, priority=0, delay_seconds=""):
        """
        发送消息到指定队列
        """
        try:
            message = (base64.b64encode(queue_data.encode())).decode()
            form_data = {
                "message": message,
                "queueName": queue_name,
                "priority": priority,
                "delaySeconds": delay_seconds
            }
            r = requests.post(f"{defaults.MQ_HOST}/rest/ms/GemMQ/sendMessage", json=form_data)
            resp = r.json()
            mob_log.info(f"spider name: {self.name}, inner ip: {inner_ip}, send message to mq success, resp: {resp}").tracker()
        except:
            mob_log.error(f"spider name: {self.name}, inner ip: {inner_ip}, send message to mq error: {traceback.format_exc()}").tracker()

    def pop_priority_queue(self, redis_key, batch_size):
        with self.server.pipeline() as pipe:
            pipe.zrevrange(redis_key, 0, batch_size - 1)
            pipe.zremrangebyrank(redis_key, -batch_size, -1)
            datas, _ = pipe.execute()
        return datas

    def latest_queue_mark(self, datas):
        """备份队列 list or hash"""
        # 1、删除上一次（多个worker，如何保证删除的一致性）
        # self.server.delete(self.latest_queue)
        self.server.hdel(self.latest_queue, inner_ip)
        # 2、 存入
        # with self.server.pipeline() as pipe:
        #     for data in datas:
        #         pipe.rpush(self.latest_queue, data)
        #     pipe.execute()
        latest_datas = []
        for data in datas:
            latest_datas.append(bytes_to_str(data))
        mob_log.info(f"spider name: {self.name}, latest_queue_mark, inner_ip: {inner_ip}, latest_datas: {latest_datas}").tracker()
        self.server.hset(self.latest_queue, inner_ip, latest_datas)

    def spider_opened_latest_pop(self):
        """绑定spider open信号； 取出 stop spider前，最后1次datas"""
        mob_log.info(f"spider name: {self.name}, spider_opened_latest_pop, inner_ip: {inner_ip}").tracker()
        if self.server.hexists(self.latest_queue, inner_ip):
            latest_datas = self.server.hget(self.latest_queue, inner_ip)
            mob_log.info(f"spider name: {self.name}, latest task back to queue, inner_ip: {inner_ip}, latest_datas: {bytes_to_str(latest_datas)}").tracker()
            self.server.hdel(self.latest_queue, inner_ip)
            for data in eval(bytes_to_str(latest_datas)):
                mob_log.info(f"spider name: {self.name}, latest task back to queue, inner_ip: {inner_ip}, data: {data}").tracker()
                if self.settings.getbool("MQ_USED", defaults.MQ_USED):  # 使用MQ
                    self.send_message2mq(queue_name=self.queue_name, queue_data=str(data), priority=1)
                else:  # 使用reids
                    self.server.lpush(self.redis_key, json.dumps(data, ensure_ascii=False))

        # if self.count_size(self.latest_queue) == 0:
        #     return
        # datas = self.fetch_data(self.latest_queue, self.redis_batch_size)

    def next_requests(self):
        """Returns a request to be scheduled or none."""
        # XXX: Do we need to use a timeout here?
        found = 0
        datas = self.fetch_data(self.redis_key, self.redis_batch_size)
        self.latest_queue_mark(datas)
        for data in datas:
            # 日志加入track_id
            try:
                queue_data = json.loads(data)
            except:
                queue_data = bytes_to_str(data)
            track_id = make_md5(queue_data)
            mob_log.info(f"spider name: {self.name}, make request from data, queue_data: {queue_data}").tracker(track_id)

            # 处理mq并发重复
            if self.settings.getbool("MQ_USED", defaults.MQ_USED):  # 使用MQ
                if self.server.exists(track_id):  # 存在则重复
                    mob_log.info(f"spider name: {self.name}, mq repetition, track_id: {track_id}").tracker(track_id)
                    continue
                else:
                    self.server.set(track_id, "1", ex=60 * 3)

            reqs = self.make_request_from_data(data)
            if isinstance(reqs, Iterable):
                for req in reqs:
                    yield req
                    # XXX: should be here?
                    found += 1
                    mob_log.info(f"start req url:{req.url}").tracker()
            elif reqs:
                yield reqs
                found += 1
            else:
                mob_log.info(f"Request not made from data: {data}").tracker()

        if found:
            mob_log.warning(f"Read {found} requests from {self.redis_key}").tracker()

    def make_request_from_data(self, data):
        """Returns a Request instance from data coming from Redis.

        By default, ``data`` is an encoded URL. You can override this method to
        provide your own message decoding.

        Parameters
        ----------
        data : bytes
            Message from redis.

        """
        url = bytes_to_str(data, self.redis_encoding)
        return self.make_requests_from_url(url)

    def schedule_next_requests(self):
        """Schedules a request if available"""
        # TODO: While there is capacity, schedule a batch of redis requests.
        for req in self.next_requests():
            self.crawler.engine.crawl(req, spider=self)

    def spider_idle(self):
        """
        Schedules a request if available, otherwise waits.
        or close spider when waiting seconds > MAX_IDLE_TIME_BEFORE_CLOSE.
        MAX_IDLE_TIME_BEFORE_CLOSE will not affect SCHEDULER_IDLE_BEFORE_CLOSE.
        """
        if self.server is not None and self.count_size(self.redis_key) > 0:
            self.spider_idle_start_time = int(time.time())

        self.schedule_next_requests()

        max_idle_time = self.settings.getint("MAX_IDLE_TIME_BEFORE_CLOSE")
        idle_time = int(time.time()) - self.spider_idle_start_time
        if max_idle_time != 0 and idle_time >= max_idle_time:
            return
        raise DontCloseSpider


class RedisSpider(RedisMixin, Spider):
    """Spider that reads urls from redis queue when idle.

    Attributes
    ----------
    redis_key : str (default: REDIS_START_URLS_KEY)
        Redis key where to fetch start URLs from..
    redis_batch_size : int (default: CONCURRENT_REQUESTS)
        Number of messages to fetch from redis on each attempt.
    redis_encoding : str (default: REDIS_ENCODING)
        Encoding to use when decoding messages from redis queue.

    Settings
    --------
    REDIS_START_URLS_KEY : str (default: "<spider.name>:start_urls")
        Default Redis key where to fetch start URLs from..
    REDIS_START_URLS_BATCH_SIZE : int (deprecated by CONCURRENT_REQUESTS)
        Default number of messages to fetch from redis on each attempt.
    REDIS_START_URLS_AS_SET : bool (default: False)
        Use SET operations to retrieve messages from the redis queue. If False,
        the messages are retrieve using the LPOP command.
    REDIS_ENCODING : str (default: "utf-8")
        Default encoding to use when decoding messages from redis queue.

    """

    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(RedisSpider, self).from_crawler(crawler, *args, **kwargs)
        obj.setup_redis(crawler)
        return obj


class RedisCrawlSpider(RedisMixin, CrawlSpider):
    """Spider that reads urls from redis queue when idle.

    Attributes
    ----------
    redis_key : str (default: REDIS_START_URLS_KEY)
        Redis key where to fetch start URLs from..
    redis_batch_size : int (default: CONCURRENT_REQUESTS)
        Number of messages to fetch from redis on each attempt.
    redis_encoding : str (default: REDIS_ENCODING)
        Encoding to use when decoding messages from redis queue.

    Settings
    --------
    REDIS_START_URLS_KEY : str (default: "<spider.name>:start_urls")
        Default Redis key where to fetch start URLs from..
    REDIS_START_URLS_BATCH_SIZE : int (deprecated by CONCURRENT_REQUESTS)
        Default number of messages to fetch from redis on each attempt.
    REDIS_START_URLS_AS_SET : bool (default: True)
        Use SET operations to retrieve messages from the redis queue.
    REDIS_ENCODING : str (default: "utf-8")
        Default encoding to use when decoding messages from redis queue.

    """

    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(RedisCrawlSpider, self).from_crawler(crawler, *args, **kwargs)
        obj.setup_redis(crawler)
        return obj

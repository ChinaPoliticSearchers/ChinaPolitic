# coding=utf-8

from peewee import *
from scrapy_redis import scheduler
from scrapy.core import scheduler

DEFAULT_PARAMS = {
    'DATABASE_DRIVER': 'mysql',
    'DATABASE_URL': 'mysql://localhost/tables',
    'DATABASE_USERNAME': 'root',
    'DATABASE_PASSWD': '88636311',
}


def get_sql_settings_from(settings):
    default_params = DEFAULT_PARAMS.copy()
    for key,value in settings.iteritems():
        default_params.update(settings.get())


class PeeweePriorityQueue(object):
    pass


class PeeweeRFPDupeFilter(object):
    pass


class Scheduler(object):
    def __init__(self, driver="sqlite",
                 url="scheduler.db",
                 username=None,
                 passwd=None,
                 queue_cls="framework.scheduler.PeeweeScheduler.PeeweePriorityQueue",
                 dupefilter_key="%(spider)s:dupefilter",
                 dupefilter_cls="framework.scheduler.PeeweeScheduler.PeeweeRFPDupeFilter",
                 idle_before_close=0):
        """
        :param driver:  database driver #sqlite,mysql,postgresql
        :param url: database url
        :param username:  database username ,if null is empty
        :param passwd:  database password,if null just be empty
        :param queue_table: queue_table settings
        :param queue_cls: queue class
        :param dupefilter_key: dupefilter key
        :param dupefilter_cls: dupefilter class
        :param idle_before_close: Timeout before giving up
        """
        if idle_before_close < 0:
            raise TypeError("idle_before_close cannot be negative")
        self.driver = driver
        self.url = url
        self.username = username
        self.passwd = passwd
        self.queue_cls = queue_cls
        self.dupefilter_key = dupefilter_key
        self.dupefilter_cls = dupefilter_cls
        self.stat = None
        self.queue = None

    def __len__(self):
        if self.queue is None:
            print("queue giving up")
            exit(1)
        return len(self.queue)

    @classmethod
    def from_settings(cls, settings):
        kwargs = {
            'flush_on_start': settings.getbool('SCHEDULER_FLUSH_ON_START'),
            'idle_before_close': settings.getint('SCHEDULER_IDLE_BEFORE_CLOSE'),
        }

        optional = {
            'queue_key': 'SCHEDULER_QUEUE_KEY',
            'queue_cls': 'SCHEDULER_QUEUE_CLASS',
            'dupefilter_key': 'SCHEDULER_DUPEFILTER_KEY',
            'dupefilter_cls': 'DUPEFILTER_CLASS',
        }

        for name, setting_name in optional.items():
            val = settings.get(setting_name)
            if val:
                kwargs[name] = val


class RedisScheduler(object):
    @classmethod
    def from_settings(cls, settings):
        kwargs = {
            'persist': settings.getbool('SCHEDULER_PERSIST'),
            'flush_on_start': settings.getbool('SCHEDULER_FLUSH_ON_START'),
            'idle_before_close': settings.getint('SCHEDULER_IDLE_BEFORE_CLOSE'),
        }

        # If these values are missing, it means we want to use the defaults.
        optional = {
            # TODO: Use custom prefixes for this settings to note that are
            # specific to scrapy-redis.
            'queue_key': 'SCHEDULER_QUEUE_KEY',
            'queue_cls': 'SCHEDULER_QUEUE_CLASS',
            'dupefilter_key': 'SCHEDULER_DUPEFILTER_KEY',
            # We use the default setting name to keep compatibility.
            'dupefilter_cls': 'DUPEFILTER_CLASS',
            'serializer': 'SCHEDULER_SERIALIZER',
        }
        for name, setting_name in optional.items():
            val = settings.get(setting_name)
            if val:
                kwargs[name] = val

        # Support serializer as a path to a module.
        if isinstance(kwargs.get('serializer'), six.string_types):
            kwargs['serializer'] = importlib.import_module(kwargs['serializer'])

        server = connection.from_settings(settings)
        # Ensure the connection is working.
        server.ping()

        return cls(server=server, **kwargs)

    @classmethod
    def from_crawler(cls, crawler):
        instance = cls.from_settings(crawler.settings)
        # FIXME: for now, stats are only supported from this constructor
        instance.stats = crawler.stats
        return instance

    def open(self, spider):
        self.spider = spider

        try:
            self.queue = load_object(self.queue_cls)(
                server=self.server,
                spider=spider,
                key=self.queue_key % {'spider': spider.name},
                serializer=self.serializer,
            )
        except TypeError as e:
            raise ValueError("Failed to instantiate queue class '%s': %s",
                             self.queue_cls, e)

        try:
            self.df = load_object(self.dupefilter_cls)(
                server=self.server,
                key=self.dupefilter_key % {'spider': spider.name},
                debug=spider.settings.getbool('DUPEFILTER_DEBUG'),
            )
        except TypeError as e:
            raise ValueError("Failed to instantiate dupefilter class '%s': %s",
                             self.dupefilter_cls, e)

        if self.flush_on_start:
            self.flush()
        # notice if there are requests already in the queue to resume the crawl
        if len(self.queue):
            spider.log("Resuming crawl (%d requests scheduled)" % len(self.queue))

    def close(self, reason):
        if not self.persist:
            self.flush()

    def flush(self):
        self.df.clear()
        self.queue.clear()

    def enqueue_request(self, request):
        if not request.dont_filter and self.df.request_seen(request):
            self.df.log(request, self.spider)
            return False
        if self.stats:
            self.stats.inc_value('scheduler/enqueued/redis', spider=self.spider)
        self.queue.push(request)
        return True

    def next_request(self):
        block_pop_timeout = self.idle_before_close
        request = self.queue.pop(block_pop_timeout)
        if request and self.stats:
            self.stats.inc_value('scheduler/dequeued/redis', spider=self.spider)
        return request

    def has_pending_requests(self):
        return len(self) > 0

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
        default_params.update(settings.getdict("REDIS_PARAMS"))



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



        def __init__database__(self):
            pass



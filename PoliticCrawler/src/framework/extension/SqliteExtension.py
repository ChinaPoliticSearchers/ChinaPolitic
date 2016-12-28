# coding=utf-8
from datetime import datetime
from scrapy.exceptions import NotConfigured
from peewee import SqliteDatabase

from framework.data_object.DataUtils import data_proxy
from framework.data_object.SpiderObject import CrawlHistory

SQLITE_DB_NAME = ""


class SqliteExtension(object):
    @staticmethod
    def from_settings(settings):
        SQLITE_DB_NAME = settings.get("SQLITE_DB_NAME")
        if not SQLITE_DB_NAME:
            raise NotConfigured

    def __init__(self):
        database_name = "history.db"
        self.data_proxy = data_proxy
        self.db = SqliteDatabase(database_name)
        self.data_proxy.initialize(self.db)

    def get_all_exists_fp(self):
        if not CrawlHistory.table_exists():
            CrawlHistory.create_table()
        crawl_urls = CrawlHistory.select(CrawlHistory.fp).where(CrawlHistory.success == True)
        crawl_urls = map(lambda crawl_url: crawl_url.url, crawl_urls)
        return crawl_urls

    def write_success_fp(self, fp):
        history = CrawlHistory()
        history.success = True
        history.timestamp = datetime.now()
        history.fp = fp

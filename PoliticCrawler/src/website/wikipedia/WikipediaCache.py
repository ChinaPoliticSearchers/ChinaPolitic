# coding=utf-8
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import re

import conf
from framework.item.HtmlItem import Website

DOWNLOAD_URL_PATH = "/home/friddle/Politics/Temp/"


class WikipediaCacheSpider(scrapy.Spider):
    name = 'wikipedia_file'
    SQLITE_DB_NAME = 'history.db'
    allowed_domains = ["www.wikipedia.com"]
    start_urls = ["https://en.wikipedia.org/wiki/Xi_Jinping"]

    def parse(self, response):
        website = Website()
        website['website_html'] = response.text
        website['website_title'] = re.search("wiki/.*$", response.url).group().replace("wiki/", "")
        website['website_tag'] = website['website_title']
        return website



setting = Settings()
setting.setmodule("conf.wikipedia_cache", priority="project")
process = CrawlerProcess(setting)
process.crawl(WikipediaCacheSpider)
process.start()
from scrapy.core.scheduler import Scheduler

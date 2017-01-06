# coding=utf-8
import scrapy
from scrapy import Request
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import re

import conf
from framework.item.HtmlItem import Website
from scrapy.contrib.linkextractors import LinkExtractor

DOWNLOAD_URL_PATH = "/home/friddle/Politics/Temp/"


class WikipediaCacheSpider(CrawlSpider):
    name = 'wikipedia_file'
    allowed_domains = ["www.wikipedia.com"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Presidents_of_the_People%27s_Republic_of_China"]
    rules = (
        Rule(LinkExtractor(allow_domains="en.wikipedia.org", restrict_xpaths="", deny=""), follow=True),
        Rule(LinkExtractor(allow_domains="en.wikipedia.org", restrict_xpaths=""), callback='parse_normal')
    )

    def parse_normal(self, response):
        #return request,items
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

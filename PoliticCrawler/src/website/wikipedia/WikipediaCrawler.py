import abc
import importlib
import os
import sys
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings
import inspect

process = CrawlerProcess(get_project_settings())

__author__ = 'friddle'
import scrapy
from scrapy.http import Request

HTTP_PROXY = "http://localhost:1081"


class BaseWikipediaCrawler(object):
    @abc.abstractmethod
    def get_parse_type(self):
        pass

    @abc.abstractmethod
    def parse(self, response, spider):
        pass


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    # allowed_domains = ["www.wikipedia.com"]
    start_urls = ["file:///home/friddle/hello.html"]

    def make_requests_from_url(self, url):
        request = Request(url=url)
        request.meta['proxy'] = HTTP_PROXY
        return request

    def parse_by_types(self, response):
        parent_name = __name__
        parent_name.replace(".WikipediaCrawler")
        parent_module_name = parent_name + ".TypeCrawler"
        file_names = os.listdir(os.path.join(os.path.dirname(__file__), "TypeCrawler"))
        crawler_type_modules = map(lambda file_name: importlib.import_module(parent_module_name + "." + file_name),
                                   file_names)
        crawler_type_module = crawler_type_modules[0]
        inspect.getmodule(crawler_type_module, inspect.isclass)

    def parse(self, response):
        self.parse_by_types(response)

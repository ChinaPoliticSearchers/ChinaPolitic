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
    @staticmethod
    def get_parse_type():
        pass

    @staticmethod
    def parse(response, spider):
        pass


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    # allowed_domains = ["www.wikipedia.com"]
    start_urls = ["file:///home/friddle/hello.html"]

    def make_requests_from_url(self, url):
        request = Request(url=url)
        request.meta['proxy'] = HTTP_PROXY
        return request

    def parse_by_types(self, type, response):
        parent_name = __name__
        parent_module_name = parent_name.replace(".WikipediaCrawler", "") + ".TypeCrawler"
        file_names = filter(lambda name: name != '__init__.py',
                            os.listdir(os.path.join(os.path.dirname(__file__), "TypeCrawler")))
        crawler_type_modules = map(
            lambda file_name: importlib.import_module(parent_module_name + "." + file_name.replace(".py", "")),
            file_names)
        crawler_type_modules = map(lambda crawler_type_module: inspect.getmembers(crawler_type_module, inspect.isclass),
                                   crawler_type_modules)
        crawler_type_classes = filter(lambda crawl_type_class: crawl_type_class.__base__ == BaseWikipediaCrawler,
                                      map(lambda crawler_type_module: crawler_type_module[1],
                                          reduce(lambda x, y: x + y, crawler_type_modules)))
        crawler_type_classes_map = {crawler_type_class.get_parse_type(): crawler_type_class for crawler_type_class
                                    in crawler_type_classes}
        crawler_type_classes_map.get(type).parse(response,None)

    def parse(self, response):
        self.parse_by_types("People", response)

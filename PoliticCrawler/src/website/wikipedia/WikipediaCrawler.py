import abc
import importlib
import os
import sys
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings
import inspect

from common_tools.reflection import common_reflections

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


def parse_by_types(parse_type, response):
    crawler_type_classes = common_reflections.get_module_all_classes("website.wikipedia.TypeCrawler", lambda
        single_class: single_class.__base__ == BaseWikipediaCrawler)
    crawler_type_classes_map = {crawler_type_class().get_parse_type(): crawler_type_class for crawler_type_class
                                in crawler_type_classes}
    crawler_type_classes_map.get(parse_type)().parse(response, None)


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    # allowed_domains = ["www.wikipedia.com"]
    start_urls = ["file:///home/friddle/hello.html"]

    def make_requests_from_url(self, url):
        request = Request(url=url)
        request.meta['proxy'] = HTTP_PROXY
        return request

    def parse(self, response):
        parse_by_types("People", response)

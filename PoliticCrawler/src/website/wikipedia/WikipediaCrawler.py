from scrapy.crawler import CrawlerProcess

from framework.util.PoliticItem import PoliticItem
from proto_struct_py.Event_pb2 import Event

__author__ = 'friddle'
import scrapy
from scrapy.http import Request

HTTP_PROXY = "http://localhost:1081"

from framework.data_pipeline.DataManagePipeline import DataManagePipeline


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    # allowed_domains = ["www.wikipedia.com"]
    start_urls = ["file:///home/friddle/hello.html"]
    custom_settings = {
        'ITEM_PIPELINES': {'framework.data_pipeline.DataManagePipeline.DataManagePipeline': 1},
        'DOWNLOADER_MIDDLEWARES': {'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100}
    }

    def make_requests_from_url(self, url):
        request = Request(url=url)
        request.meta['proxy'] = HTTP_PROXY
        return request

    def parse(self, response):
        politic_item = PoliticItem()
        politic_item["event"] = Event(event_id="sdfsdfsdfsdf", event_name="helloworld")
        return politic_item


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(WikipediaSpider)
process.start()

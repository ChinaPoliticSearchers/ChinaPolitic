# coding=utf-8
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from website.wikipedia.WikipediaCrawler import WikipediaSpider


def start_wikipedia_crawler():
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    process = CrawlerProcess(get_project_settings())
    process.crawl(WikipediaSpider)
    process.start()

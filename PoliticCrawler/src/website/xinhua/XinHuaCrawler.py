from scrapy.crawler import CrawlerProcess

__author__ = 'friddle'
import scrapy


class XinHuaSpider(scrapy.Spider):
    name = "xinhua"
    allowed_domains = ["news.xinhuanet.com"]
    start_urls = [
        "http://news.xinhuanet.com/rwk/2013-02/01/c_114586554.htm"
    ]

    ITEM_PIPELINES = [
        'framework.data_pipeline.StructPipeline',
    ]

    def parse(self, response):
        text = response.xpath('//p/text()').extract()
        print(text)
        return None


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(XinHuaSpider)
process.start()

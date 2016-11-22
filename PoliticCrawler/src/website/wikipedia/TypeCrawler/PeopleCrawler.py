# coding=utf-8
from website.wikipedia.WikipediaCrawler import BaseWikipediaCrawler


class PeopleCrawler(BaseWikipediaCrawler):
    @staticmethod
    def parse(response, spider):
        web_text=response.xpath("//text()").extract()
        print("pretented i am invoke")
        return None

    @staticmethod
    def get_parse_type():
        return "People"

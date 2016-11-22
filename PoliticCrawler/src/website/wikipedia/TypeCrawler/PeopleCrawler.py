# coding=utf-8
from website.wikipedia.WikipediaCrawler import BaseWikipediaCrawler


class PeopleCrawler(BaseWikipediaCrawler):
    def parse(self,response, spider):
        web_text=response.xpath("//text()").extract()
        print("pretented i am invoke")
        return None

    def get_parse_type(self):
        return "People"

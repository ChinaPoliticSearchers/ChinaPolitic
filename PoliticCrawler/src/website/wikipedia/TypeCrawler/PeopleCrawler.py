# coding=utf-8
from website.wikipedia.WikipediaCrawler import BaseWikipediaCrawler


class PeopleCrawler(BaseWikipediaCrawler):
    def parse(self, response):
        return None

    def get_parse_type(self):
        return "People"

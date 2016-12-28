# coding=utf-8
from scrapy import Item
from scrapy import Field


class Website(Item):
    website_html = Field()
    website_title = Field()
    website_tag = Field()

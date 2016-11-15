# coding=utf-8
from scrapy import Field
from scrapy import Item


class PoliticItem(Item):
    event = Field()
    job_title = Field()
    judge = Field()
    organization = Field()
    people = Field()
    Relationship = Field()
    source = Field()


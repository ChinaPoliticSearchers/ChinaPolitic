# coding=utf-8
from peewee import *

from framework.data_object.DataUtils import BaseModel


class CrawlHistory(BaseModel):
    timestamp = DateField()
    fp = CharField(unique=True)
    success = BooleanField(default=True)
    error_message = CharField(default=None)

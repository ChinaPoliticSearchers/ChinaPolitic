# coding=utf-8

# write a base class wrap peewee and fields
from peewee import Proxy, Model

data_proxy = Proxy()


class BaseModel(Model):
    class Meta:
        db = data_proxy

# coding=utf-8
import six

from scrapy import Field
from scrapy import Item
from scrapy.item import ItemMeta, DictItem

from common_tools.reflection import reflection_tools


@six.add_metaclass(ItemMeta)
class PoliticItem(DictItem):
    def __init__(self):
        for name in reflection_tools.data_class_name:
            self._values = {}
            self.fields[name] = Field()

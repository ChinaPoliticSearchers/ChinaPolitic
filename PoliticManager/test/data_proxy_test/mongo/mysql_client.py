# coding=utf-8
import unittest

from data_proxy_test import basic
from data_proxy.mongodb.mongo_proxy import MongoDataManage


class MongoProxyTest(basic.BASIC_DATA_TEST):
    def get_proxy_object(self):
        return MongoDataManage()


if __name__ == '__main__':
    unittest.main()

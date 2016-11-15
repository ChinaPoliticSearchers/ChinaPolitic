# coding=utf-8
import unittest

from data_proxy_test import basic
from data_proxy.mysql.mysql_proxy import MysqlDataManage


class MysqlProxyTest(basic.BASIC_DATA_TEST):
    def get_proxy_object(self):
        return MysqlDataManage()


if __name__ == '__main__':
    unittest.main()

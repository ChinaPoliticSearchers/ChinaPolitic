__author__ = 'friddle'

from pymongo import MongoClient
from common.basic_proxy import  BasicDataManage


class MongoDataManage(BasicDataManage):
    def __init__(self):
        self.mongo_client = MongoClient('localhost', 27017)

    def save_detail(self, type_name, to_save_object, insert_optionals):
        print("pretended to invoke")
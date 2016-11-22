#coding=utf-8
__author__ = 'friddle'

from pymongo import MongoClient
from common.basic_proxy import  BasicDataManage
#from common.reflection_tools import is_data_name_acceptable, get_instant_object
from proto_data_interface_py.BasicDataManage_pb2 import DataResponse, Error, Level
from logging import Logger
import datetime

class MongoDataManage(BasicDataManage):
    def __init__(self):
        self.mongo_client = MongoClient('localhost', 27017)
        db = self.mongo_client.test_database    #建库
        collection = db.test_collection    #建集合
        posts = db.posts   #插入文件

    def save_detail(self, type_name, to_save_object, insert_optionals):
        post = {
            'typename':type_name,
            'to_save_object':to_save_object,
            'insert_optionals':insert_optionals
        }
        posts = self.db.posts
        post_id = posts.insert_one(post).inserted_id
        print("pretended to invoke")
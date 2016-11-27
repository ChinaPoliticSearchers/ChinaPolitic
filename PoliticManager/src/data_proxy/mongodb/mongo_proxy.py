# coding=utf-8
__author__ = 'friddle'

from pymongo import MongoClient
from common.basic_proxy import BasicDataManage
from proto_data_interface_py import BasicDataManage_pb2
from google.protobuf.json_format import MessageToJson
import simplejson

MONGO_HOST = 'localhost'
MONGO_PORT = 27017


class MongoDataManage(BasicDataManage):
    def __init__(self):
        self.mongo_client = MongoClient(MONGO_HOST, MONGO_PORT)
        self.politic_db = self.mongo_client["politic_db"]  # 建库

    def set_post_id(self, data_obj):
        data_obj=simplejson.load({'ddd':'test'})

    def save_detail(self, type_name, to_save_object, insert_optionals):
        db_names = self.politic_db.collection_names()
        collection = self.politic_db[type_name]
        if type_name not in db_names:
            pass
            # add index
        post = MessageToJson(to_save_object)
        # need to set all kind of id to _id and keep the old one
        post = simplejson.loads(str(post).replace("eventId", "_id"))
        event_id = collection.insert_one(post).inserted_id
        return True, "id:" + str(event_id)

# coding=utf-8
__author__ = 'friddle'

from pymongo import MongoClient
from common.basic_proxy import BasicDataManage
from google.protobuf.json_format import MessageToJson
import simplejson

MONGO_HOST = 'localhost'
MONGO_PORT = 27017


class MongoDataManage(BasicDataManage):
    def __init__(self):
        self.mongo_client = MongoClient(MONGO_HOST, MONGO_PORT)
        self.politic_db = self.mongo_client["politic_db"]  # 建库

    def save_detail(self, type_name, to_save_object, insert_optionals):
        db_names = self.politic_db.collection_names()
        collection = self.politic_db[type_name]
        if type_name not in db_names:
            pass
            # add index
        post = MessageToJson(to_save_object)
        # need regex to change all type
        post = simplejson.loads(str(post).replace("eventId", "_id"))
        event_id = collection.insert_one(post).inserted_id
        return True, "event_id" + str(event_id)



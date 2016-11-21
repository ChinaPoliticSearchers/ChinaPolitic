import logging

import sys

from proto_data_interface_py.BasicDataManage_pb2 import InsertData, DataServiceStub, InsertOptional


class DataManagePipeline(object):
    def __init__(self):
        pass

    @staticmethod
    def check_items(self, typename, item):
        pass

    @staticmethod
    def insert_items(typename, politic_obj):
        insert_data = InsertData(insert_type_name=typename, insert_bytes=politic_obj.SerializeToString(),
                                 insert_optionals=[InsertOptional.Value("generate_id")])
        data_response = DataServiceStub.Insert(insert_data)
        if not data_response.success:
            logging.error("insert database error")
            sys.exit(0)

    def process_item(self, politic_item, spider):
        for field_name in politic_item.fields:
            if field_name in politic_item.keys():
                self.insert_items(field_name, politic_item[field_name])

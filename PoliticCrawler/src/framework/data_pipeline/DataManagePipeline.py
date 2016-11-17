from scrapy import signals

from scrapy.pipelines.files import FilesPipeline
from proto_data_interface_py.BasicDataManage_pb2 import BetaDataServiceStub




class DataManagePipeline(object):
    def __init__(self):
        pass

    def check_items(self, item):
        pass


    def insert_items(self,typename,item):
        BetaDataServiceStub.Insert()

    def process_item(self, item, spider):
        self.check_items(item)
        print(item)
        return item

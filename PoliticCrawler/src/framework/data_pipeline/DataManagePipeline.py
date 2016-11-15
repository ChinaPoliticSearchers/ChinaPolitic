from scrapy import signals

class DataManagePipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        print("I am process it")

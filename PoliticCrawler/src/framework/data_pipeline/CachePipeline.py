#  coding=utf-8
import os
from scrapy.settings import Settings

FILE_TEMP_PATH = "/home/friddle/temp/"


class FilePipeline(object):
    @staticmethod
    def from_settings(settings):
        print("from_settings:" + str(settings.get("DOWNLOAD_URL_PATH")))

    def __init__(self):
        print("__init__")
        self.WEBSITE_LOC = FILE_TEMP_PATH

    def process_item(self, item, spider):
        location = os.path.join(FILE_TEMP_PATH, item['website_title'] + ".html")
        if not os.path.exists(os.path.dirname(location)):
            os.mkdirs(os.path.dirname(location))
        with open(location, "w+") as website_files:
            website_files.write(item['website_html'].encode("utf-8"))
            website_files.flush()

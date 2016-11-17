# coding=utf-8
import hashlib

from common_tools.generate_id.types.basic import BasicGenerator


class EventGenerate(BasicGenerator):
    def GenerateId(self, event):
        return hashlib.md5(event.event_name)


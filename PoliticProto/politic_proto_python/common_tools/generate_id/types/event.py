# coding=utf-8
import hashlib

from common_tools.generate_id.generator import BasicGenerator


class EventGenerate(BasicGenerator):
    def GetGenerateType(self):
        return "Event"

    def GenerateId(self, event):
        return hashlib.md5(event.event_name).hexdigest


# coding=utf-8
import abc

import importlib
import inspect
import os

from proto_common_tools_py import IdGenerate_pb2


class IdGeneratorMD5(IdGenerate_pb2.Id_GenerateServicer):
    def __init__(self):
        packages = "common_tools.generate_id.types"
        files = os.listdir(inspect.getfile(importlib.import_module(packages)))
        self.generate_classes = inspect.getmembers(importlib.import_module(files), inspect.isclass)

    def GenerateId(self, generate_req, context):
        generate_class = filter(lambda name: name[0].lowercase.equals(generate_req.generateIdType), self.generate_classes)[0]




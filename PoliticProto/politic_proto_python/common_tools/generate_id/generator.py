# coding=utf-8
import sys

from common_tools.reflection import reflections_tools
from proto_common_tools_py import IdGenerate_pb2

from logging import Logger
import abc


class BasicGenerator(object):
    @abc.abstractmethod
    def GenerateId(self, to_id_object):
        pass

    @abc.abstractmethod
    def GetGenerateType(self):
        pass

    @abc.abstractmethod
    def GetObjectKey(self):
        pass

    def GetGenerateObject(self,gen_object):
        self.GetObjectKey()


class IdGeneratorMD5(IdGenerate_pb2.Id_GenerateServicer):
    def __init__(self):
        packages = "common_tools.generate_id.types"
        generate_classes = reflections_tools.get_module_all_classes(packages,
                                                                    lambda classes: classes.__base__ == BasicGenerator)
        self.generate_class = {single_class().GenerateType(): single_class for single_class in generate_classes}

    def generate_object(self, gen_type, gen_object):
        if gen_type in self.generate_class:
            return self.generate_class.get(gen_type).GenerateId(gen_object)
        else:
            Logger.error("Warnning not for generate id")
            sys.exit(0)

    def GenerateId(self, generate_req, context):
        pass

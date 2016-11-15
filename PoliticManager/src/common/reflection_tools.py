# coding=utf-8

import inspect
import os
import sys
from logging import Logger
import importlib

DATA_STRUCT_MODULE = "proto_struct_py"
__import__(DATA_STRUCT_MODULE)

if not sys.modules.has_key(DATA_STRUCT_MODULE):
    Logger.error("proto_struct_py is not found")
    sys.exit(0)

get_class_member = lambda member: inspect.getmembers(member, inspect.isclass)
source_path = os.path.dirname(inspect.getfile(sys.modules[DATA_STRUCT_MODULE]))
data_class_files = filter(lambda x: x.endswith("pb2.py"), os.listdir(source_path))
data_class_modules = map(
    lambda file_name: importlib.import_module(DATA_STRUCT_MODULE + "." + inspect.getmodulename(file_name)),
    data_class_files)

data_class_members = reduce(lambda begin, after_list: begin + after_list, map(get_class_member, data_class_modules))
data_class_name = map(lambda class_member: class_member[0], data_class_members)


def get_instant_object(data_name):
    data_class = filter(lambda class_member: class_member[0] == data_name, data_class_members)[0]
    return data_class[1]()


def is_data_name_acceptable(data_name):
    if data_name in data_class_name:
        return True
    else:
        return False






# coding=utf-8
import importlib
import inspect
import os

import sys
from google.protobuf.message import Message


def get_module_all_classes(modules_name, filter_func=None):
    importlib.import_module(modules_name)
    base_module = sys.modules[modules_name]
    file_names = filter(lambda name: name != '__init__.py' and not name.endswith("pyc"),
                        os.listdir(os.path.dirname(inspect.getabsfile(base_module))))
    type_modules = map(
        lambda file_name: importlib.import_module(modules_name + "." + file_name.replace(".py", "")),
        file_names)
    type_modules = map(lambda type_module: inspect.getmembers(type_module, inspect.isclass), type_modules)
    if filter_func is None: filter_func = lambda x: True
    type_classes = filter(lambda type_class: filter_func(type_class),
                          map(lambda type_module: type_module[1],
                              reduce(lambda x, y: x + y, type_modules)))
    return type_classes


classes = get_module_all_classes("proto_struct_py", lambda single_class: single_class.__base__ == Message)
# classes = get_module_all_classes("proto_struct_py")
print(classes)

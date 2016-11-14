# coding=utf-8

import inspect
import sys
from logging import Logger

DATA_STRUCT_MODULE = "proto_struct_py"
__import__(DATA_STRUCT_MODULE)

if not sys.modules.has_key(DATA_STRUCT_MODULE):
    Logger.error("proto_struct_py is not found")
    sys.exit(0)



class_es = inspect.getmembers(sys.modules[DATA_STRUCT_MODULE])
print(class_es)




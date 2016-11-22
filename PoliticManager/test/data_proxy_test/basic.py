# coding=utf-8
import abc
import hashlib
import threading
import time
import unittest

import grpc
from concurrent import futures

from proto_data_interface_py import BasicDataManage_pb2
from proto_struct_py import Event_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
PORT = 10087


class BASIC_DATA_TEST(unittest.TestCase):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_proxy_object(self):
        pass

    def run_serve(self):
        self.stop = False
        data_service = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        BasicDataManage_pb2.add_DataServiceServicer_to_server(self.get_proxy_object(), data_service)
        data_service.add_insecure_port('[::]:' + str(PORT))
        data_service.start()
        while not self.stop:
            time.sleep(1)

    def setUp(self):
        channel = grpc.insecure_channel('localhost:' + str(PORT))
        data_service_thread = threading.Thread(target=self.run_serve, args=())
        data_service_thread.start()
        time.sleep(1)
        self.data_stub = BasicDataManage_pb2.DataServiceStub(channel)

    def test_insertData(self):
        event = Event_pb2.Event(event_id=hashlib.md5("test fuck").hexdigest(), event_name="fuck you")
        response = self.data_stub.Insert(
            BasicDataManage_pb2.InsertData(insert_type_name='Event', insert_bytes=event.SerializeToString(),
                                           insert_optionals=[
                                               BasicDataManage_pb2.InsertOptional.Value(
                                                   "override")]))
        print(response.success)
        if response.success is False:
            print(response.error.message)

    def tearDown(self):
        self.stop = True



# coding=utf-8
import threading
from threading import Thread

import grpc
import time


from data_proxy.mysql.mysql_proxy import BasicDataManage
from proto_data_interface_py import BasicDataManage_pb2
from proto_struct_py import Event_pb2
import unittest

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MYSQL_PROXY_TEST(unittest.TestCase):
    def run_serve(self):
        self.stop = False
        data_service = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        BasicDataManage_pb2.add_DataServiceServicer_to_server(BasicDataManage(), data_service)
        data_service.add_insecure_port('[::]:10086')
        data_service.start()
        while not self.stop:
            time.sleep(1)

    def setUp(self):
        channel = grpc.insecure_channel('localhost:10086')
        data_service_thread = threading.Thread(target=self.run_serve, args=())
        # data_service_thread.daemon = False
        data_service_thread.start()
        self.data_stub = BasicDataManage_pb2.DataServiceStub(channel)

    def test_insertData(self):
        event = Event_pb2.Event(event_id=-1, event_name="fuck you")
        response = self.data_stub.Insert(BasicDataManage_pb2.InsertData(insert_type_name='event', insert_bytes=event.SerializeToString(),
                                                                        insert_optionals=[
                                                                            BasicDataManage_pb2.InsertOptional.Value(
                                                                                "override")]))
        print("success")
        self.assertEqual(response.success, True, "return success")

    def tearDown(self):
        self.stop = True


if __name__ == '__main__':
    # run_serve()
    unittest.main()

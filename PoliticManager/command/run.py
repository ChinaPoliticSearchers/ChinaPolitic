# coding=utf-8
import grpc
from concurrent import futures
import time

from proto_data_interface_py import BasicDataManage_pb2

PORT = 10087
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def run_serve():
    data_service = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    BasicDataManage_pb2.add_DataServiceServicer_to_server(self.get_proxy_object(), data_service)
    data_service.add_insecure_port('[::]:' + str(PORT))
    data_service.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt as e:
        print e

run_serve()
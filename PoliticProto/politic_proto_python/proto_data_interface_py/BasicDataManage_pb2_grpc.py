import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import BasicDataManage_pb2 as BasicDataManage__pb2
import BasicDataManage_pb2 as BasicDataManage__pb2
import BasicDataManage_pb2 as BasicDataManage__pb2
import BasicDataManage_pb2 as BasicDataManage__pb2
import BasicDataManage_pb2 as BasicDataManage__pb2
import BasicDataManage_pb2 as BasicDataManage__pb2
import BasicDataManage_pb2 as BasicDataManage__pb2
import BasicDataManage_pb2 as BasicDataManage__pb2


class DataServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Insert = channel.unary_unary(
        '/DataService/Insert',
        request_serializer=BasicDataManage__pb2.InsertData.SerializeToString,
        response_deserializer=BasicDataManage__pb2.DataResponse.FromString,
        )
    self.Query = channel.unary_unary(
        '/DataService/Query',
        request_serializer=BasicDataManage__pb2.QueryData.SerializeToString,
        response_deserializer=BasicDataManage__pb2.DataResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/DataService/Delete',
        request_serializer=BasicDataManage__pb2.QueryData.SerializeToString,
        response_deserializer=BasicDataManage__pb2.DataResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/DataService/Update',
        request_serializer=BasicDataManage__pb2.UpdateData.SerializeToString,
        response_deserializer=BasicDataManage__pb2.DataResponse.FromString,
        )


class DataServiceServicer(object):

  def Insert(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Query(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Insert': grpc.unary_unary_rpc_method_handler(
          servicer.Insert,
          request_deserializer=BasicDataManage__pb2.InsertData.FromString,
          response_serializer=BasicDataManage__pb2.DataResponse.SerializeToString,
      ),
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=BasicDataManage__pb2.QueryData.FromString,
          response_serializer=BasicDataManage__pb2.DataResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=BasicDataManage__pb2.QueryData.FromString,
          response_serializer=BasicDataManage__pb2.DataResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=BasicDataManage__pb2.UpdateData.FromString,
          response_serializer=BasicDataManage__pb2.DataResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DataService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

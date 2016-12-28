import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import IdGenerate_pb2 as IdGenerate__pb2
import IdGenerate_pb2 as IdGenerate__pb2


class Id_GenerateStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GenerateId = channel.unary_unary(
        '/Id_Generate/GenerateId',
        request_serializer=IdGenerate__pb2.GenerateIdRequest.SerializeToString,
        response_deserializer=IdGenerate__pb2.GenerateIdResponse.FromString,
        )


class Id_GenerateServicer(object):

  def GenerateId(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_Id_GenerateServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GenerateId': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateId,
          request_deserializer=IdGenerate__pb2.GenerateIdRequest.FromString,
          response_serializer=IdGenerate__pb2.GenerateIdResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Id_Generate', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

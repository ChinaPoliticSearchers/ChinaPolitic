# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BasicDataManage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BasicDataManage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x15\x42\x61sicDataManage.proto\"\x82\x01\n\x05\x45rror\x12\r\n\x05\x65rror\x18\x01 \x02(\t\x12\r\n\x05stack\x18\x02 \x01(\t\x12\x0b\n\x03\x65nv\x18\x03 \x01(\t\x12\x1b\n\x05level\x18\x04 \x02(\x0e\x32\x0c.Error.Level\"1\n\x05Level\x12\t\n\x05\x44\x45\x42UG\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x08\n\x04WARN\x10\x02\x12\t\n\x05\x45RROR\x10\x03\"i\n\x0c\x44\x61taResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x15\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x06.Error\x12\x1a\n\x12response_type_name\x18\x02 \x02(\t\x12\x15\n\rresponse_byte\x18\x04 \x03(\x0c\"g\n\nInsertData\x12\x18\n\x10insert_type_name\x18\x01 \x02(\t\x12\x14\n\x0cinsert_bytes\x18\x02 \x02(\x0c\x12)\n\x10insert_optionals\x18\x03 \x03(\x0e\x32\x0f.InsertOptional\"V\n\tQueryData\x12\x17\n\x0fquery_type_name\x18\x01 \x02(\t\x12\r\n\x05limit\x18\x02 \x02(\x03\x12\x0c\n\x04keys\x18\x03 \x03(\t\x12\x13\n\x0bquery_bytes\x18\x04 \x02(\x0c\"j\n\nUpdateData\x12\x18\n\x04\x64\x61ta\x18\x01 \x02(\x0b\x32\n.QueryData\x12\x12\n\nupdate_key\x18\x02 \x02(\t\x12\x15\n\rupdate_values\x18\x03 \x02(\x0c\x12\x17\n\x04type\x18\x04 \x02(\x0e\x32\t.DATATYPE*W\n\x08\x44\x41TATYPE\x12\x0b\n\x07\x42OOLEAN\x10\x00\x12\x07\n\x03INT\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\t\n\x05\x46LOAT\x10\x03\x12\x08\n\x04LONG\x10\x04\x12\n\n\x06STRING\x10\x05\x12\x08\n\x04\x42YTE\x10\x06*2\n\x0eInsertOptional\x12\x12\n\x0e\x61uto_increment\x10\x00\x12\x0c\n\x08override\x10\x01\x32\xa2\x01\n\x0b\x44\x61taService\x12$\n\x06Insert\x12\x0b.InsertData\x1a\r.DataResponse\x12\"\n\x05Query\x12\n.QueryData\x1a\r.DataResponse\x12#\n\x06\x44\x65lete\x12\n.QueryData\x1a\r.DataResponse\x12$\n\x06Update\x12\x0b.UpdateData\x1a\r.DataResponse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_DATATYPE = _descriptor.EnumDescriptor(
  name='DATATYPE',
  full_name='DATATYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LONG', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BYTE', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=566,
  serialized_end=653,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DATATYPE = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
_INSERTOPTIONAL = _descriptor.EnumDescriptor(
  name='InsertOptional',
  full_name='InsertOptional',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='auto_increment', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='override', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=655,
  serialized_end=705,
)
_sym_db.RegisterEnumDescriptor(_INSERTOPTIONAL)

InsertOptional = enum_type_wrapper.EnumTypeWrapper(_INSERTOPTIONAL)
BOOLEAN = 0
INT = 1
DOUBLE = 2
FLOAT = 3
LONG = 4
STRING = 5
BYTE = 6
auto_increment = 0
override = 1


_ERROR_LEVEL = _descriptor.EnumDescriptor(
  name='Level',
  full_name='Error.Level',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=107,
  serialized_end=156,
)
_sym_db.RegisterEnumDescriptor(_ERROR_LEVEL)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='Error.error', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stack', full_name='Error.stack', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='env', full_name='Error.env', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Error.level', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERROR_LEVEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=156,
)


_DATARESPONSE = _descriptor.Descriptor(
  name='DataResponse',
  full_name='DataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='DataResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='DataResponse.error', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_type_name', full_name='DataResponse.response_type_name', index=2,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_byte', full_name='DataResponse.response_byte', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=263,
)


_INSERTDATA = _descriptor.Descriptor(
  name='InsertData',
  full_name='InsertData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='insert_type_name', full_name='InsertData.insert_type_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='insert_bytes', full_name='InsertData.insert_bytes', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='insert_optionals', full_name='InsertData.insert_optionals', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=368,
)


_QUERYDATA = _descriptor.Descriptor(
  name='QueryData',
  full_name='QueryData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_type_name', full_name='QueryData.query_type_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='QueryData.limit', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keys', full_name='QueryData.keys', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query_bytes', full_name='QueryData.query_bytes', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=370,
  serialized_end=456,
)


_UPDATEDATA = _descriptor.Descriptor(
  name='UpdateData',
  full_name='UpdateData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='UpdateData.data', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_key', full_name='UpdateData.update_key', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_values', full_name='UpdateData.update_values', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='UpdateData.type', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=458,
  serialized_end=564,
)

_ERROR.fields_by_name['level'].enum_type = _ERROR_LEVEL
_ERROR_LEVEL.containing_type = _ERROR
_DATARESPONSE.fields_by_name['error'].message_type = _ERROR
_INSERTDATA.fields_by_name['insert_optionals'].enum_type = _INSERTOPTIONAL
_UPDATEDATA.fields_by_name['data'].message_type = _QUERYDATA
_UPDATEDATA.fields_by_name['type'].enum_type = _DATATYPE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['DataResponse'] = _DATARESPONSE
DESCRIPTOR.message_types_by_name['InsertData'] = _INSERTDATA
DESCRIPTOR.message_types_by_name['QueryData'] = _QUERYDATA
DESCRIPTOR.message_types_by_name['UpdateData'] = _UPDATEDATA
DESCRIPTOR.enum_types_by_name['DATATYPE'] = _DATATYPE
DESCRIPTOR.enum_types_by_name['InsertOptional'] = _INSERTOPTIONAL

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'BasicDataManage_pb2'
  # @@protoc_insertion_point(class_scope:Error)
  ))
_sym_db.RegisterMessage(Error)

DataResponse = _reflection.GeneratedProtocolMessageType('DataResponse', (_message.Message,), dict(
  DESCRIPTOR = _DATARESPONSE,
  __module__ = 'BasicDataManage_pb2'
  # @@protoc_insertion_point(class_scope:DataResponse)
  ))
_sym_db.RegisterMessage(DataResponse)

InsertData = _reflection.GeneratedProtocolMessageType('InsertData', (_message.Message,), dict(
  DESCRIPTOR = _INSERTDATA,
  __module__ = 'BasicDataManage_pb2'
  # @@protoc_insertion_point(class_scope:InsertData)
  ))
_sym_db.RegisterMessage(InsertData)

QueryData = _reflection.GeneratedProtocolMessageType('QueryData', (_message.Message,), dict(
  DESCRIPTOR = _QUERYDATA,
  __module__ = 'BasicDataManage_pb2'
  # @@protoc_insertion_point(class_scope:QueryData)
  ))
_sym_db.RegisterMessage(QueryData)

UpdateData = _reflection.GeneratedProtocolMessageType('UpdateData', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEDATA,
  __module__ = 'BasicDataManage_pb2'
  # @@protoc_insertion_point(class_scope:UpdateData)
  ))
_sym_db.RegisterMessage(UpdateData)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class DataServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Insert = channel.unary_unary(
        '/DataService/Insert',
        request_serializer=InsertData.SerializeToString,
        response_deserializer=DataResponse.FromString,
        )
    self.Query = channel.unary_unary(
        '/DataService/Query',
        request_serializer=QueryData.SerializeToString,
        response_deserializer=DataResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/DataService/Delete',
        request_serializer=QueryData.SerializeToString,
        response_deserializer=DataResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/DataService/Update',
        request_serializer=UpdateData.SerializeToString,
        response_deserializer=DataResponse.FromString,
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
          request_deserializer=InsertData.FromString,
          response_serializer=DataResponse.SerializeToString,
      ),
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=QueryData.FromString,
          response_serializer=DataResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=QueryData.FromString,
          response_serializer=DataResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=UpdateData.FromString,
          response_serializer=DataResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DataService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaDataServiceServicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def Insert(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Query(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Delete(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Update(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaDataServiceStub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def Insert(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Insert.future = None
  def Query(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Query.future = None
  def Delete(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Delete.future = None
  def Update(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Update.future = None


def beta_create_DataService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('DataService', 'Delete'): QueryData.FromString,
    ('DataService', 'Insert'): InsertData.FromString,
    ('DataService', 'Query'): QueryData.FromString,
    ('DataService', 'Update'): UpdateData.FromString,
  }
  response_serializers = {
    ('DataService', 'Delete'): DataResponse.SerializeToString,
    ('DataService', 'Insert'): DataResponse.SerializeToString,
    ('DataService', 'Query'): DataResponse.SerializeToString,
    ('DataService', 'Update'): DataResponse.SerializeToString,
  }
  method_implementations = {
    ('DataService', 'Delete'): face_utilities.unary_unary_inline(servicer.Delete),
    ('DataService', 'Insert'): face_utilities.unary_unary_inline(servicer.Insert),
    ('DataService', 'Query'): face_utilities.unary_unary_inline(servicer.Query),
    ('DataService', 'Update'): face_utilities.unary_unary_inline(servicer.Update),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_DataService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('DataService', 'Delete'): QueryData.SerializeToString,
    ('DataService', 'Insert'): InsertData.SerializeToString,
    ('DataService', 'Query'): QueryData.SerializeToString,
    ('DataService', 'Update'): UpdateData.SerializeToString,
  }
  response_deserializers = {
    ('DataService', 'Delete'): DataResponse.FromString,
    ('DataService', 'Insert'): DataResponse.FromString,
    ('DataService', 'Query'): DataResponse.FromString,
    ('DataService', 'Update'): DataResponse.FromString,
  }
  cardinalities = {
    'Delete': cardinality.Cardinality.UNARY_UNARY,
    'Insert': cardinality.Cardinality.UNARY_UNARY,
    'Query': cardinality.Cardinality.UNARY_UNARY,
    'Update': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'DataService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Source.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Source.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0cSource.proto\"\x17\n\x06Source\x12\r\n\x05links\x18\x01 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='links', full_name='Source.links', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=16,
  serialized_end=39,
)

DESCRIPTOR.message_types_by_name['Source'] = _SOURCE

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), dict(
  DESCRIPTOR = _SOURCE,
  __module__ = 'Source_pb2'
  # @@protoc_insertion_point(class_scope:Source)
  ))
_sym_db.RegisterMessage(Source)


# @@protoc_insertion_point(module_scope)

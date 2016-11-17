# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: JobTitle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='JobTitle.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0eJobTitle.proto\x1a\x0c\x43ommon.proto\"\xcb\x01\n\x08JobTitle\x12\x0e\n\x06job_id\x18\x01 \x02(\t\x12\x10\n\x08job_name\x18\x02 \x03(\t\x12%\n\x06served\x18\x03 \x03(\x0b\x32\x15.JobTitle.ServedEntry\x12\x16\n\x0eorganzation_id\x18\x04 \x02(\t\x12\x11\n\tevents_id\x18\x05 \x03(\t\x12\x11\n\tjudges_id\x18\x06 \x03(\t\x1a\x38\n\x0bServedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.Duration:\x02\x38\x01')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_JOBTITLE_SERVEDENTRY = _descriptor.Descriptor(
  name='ServedEntry',
  full_name='JobTitle.ServedEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='JobTitle.ServedEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='JobTitle.ServedEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=236,
)

_JOBTITLE = _descriptor.Descriptor(
  name='JobTitle',
  full_name='JobTitle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='JobTitle.job_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job_name', full_name='JobTitle.job_name', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='served', full_name='JobTitle.served', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='organzation_id', full_name='JobTitle.organzation_id', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='events_id', full_name='JobTitle.events_id', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='judges_id', full_name='JobTitle.judges_id', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_JOBTITLE_SERVEDENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=236,
)

_JOBTITLE_SERVEDENTRY.fields_by_name['value'].message_type = Common__pb2._DURATION
_JOBTITLE_SERVEDENTRY.containing_type = _JOBTITLE
_JOBTITLE.fields_by_name['served'].message_type = _JOBTITLE_SERVEDENTRY
DESCRIPTOR.message_types_by_name['JobTitle'] = _JOBTITLE

JobTitle = _reflection.GeneratedProtocolMessageType('JobTitle', (_message.Message,), dict(

  ServedEntry = _reflection.GeneratedProtocolMessageType('ServedEntry', (_message.Message,), dict(
    DESCRIPTOR = _JOBTITLE_SERVEDENTRY,
    __module__ = 'JobTitle_pb2'
    # @@protoc_insertion_point(class_scope:JobTitle.ServedEntry)
    ))
  ,
  DESCRIPTOR = _JOBTITLE,
  __module__ = 'JobTitle_pb2'
  # @@protoc_insertion_point(class_scope:JobTitle)
  ))
_sym_db.RegisterMessage(JobTitle)
_sym_db.RegisterMessage(JobTitle.ServedEntry)


_JOBTITLE_SERVEDENTRY.has_options = True
_JOBTITLE_SERVEDENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventoryService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import book_pb2 as book__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16inventoryService.proto\x1a\nbook.proto\"^\n\rCreateRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\x17\n\x0fpublishing_year\x18\x03 \x01(\x05\x12\x15\n\x05genre\x18\x04 \x01(\x0e\x32\x06.Genre\"\x1b\n\x0b\x43reateReply\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"\x1a\n\nGetRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"\x1f\n\x08GetReply\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book2e\n\x10InventoryService\x12,\n\nCreateBook\x12\x0e.CreateRequest\x1a\x0c.CreateReply\"\x00\x12#\n\x07GetBook\x12\x0b.GetRequest\x1a\t.GetReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventoryService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEREQUEST._serialized_start=38
  _CREATEREQUEST._serialized_end=132
  _CREATEREPLY._serialized_start=134
  _CREATEREPLY._serialized_end=161
  _GETREQUEST._serialized_start=163
  _GETREQUEST._serialized_end=189
  _GETREPLY._serialized_start=191
  _GETREPLY._serialized_end=222
  _INVENTORYSERVICE._serialized_start=224
  _INVENTORYSERVICE._serialized_end=325
# @@protoc_insertion_point(module_scope)

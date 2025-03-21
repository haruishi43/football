# coding=utf-8
# Copyright 2019 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gfootball/eval_server/proto/master.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="gfootball/eval_server/proto/master.proto",
    package="gfootball.eval_server",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n(gfootball/eval_server/proto/master.proto\x12\x15gfootball.eval_server"x\n\x10StartGameRequest\x12\x14\n\x0cgame_version\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\x12\x12\n\nmodel_name\x18\x04 \x01(\t\x12\x19\n\x11include_rendering\x18\x05 \x01(\x08"A\n\x11StartGameResponse\x12\x1b\n\x13game_server_address\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\t2j\n\x06Master\x12`\n\tStartGame\x12\'.gfootball.eval_server.StartGameRequest\x1a(.gfootball.eval_server.StartGameResponse"\x00\x62\x06proto3'
    ),
)


_STARTGAMEREQUEST = _descriptor.Descriptor(
    name="StartGameRequest",
    full_name="gfootball.eval_server.StartGameRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="game_version",
            full_name="gfootball.eval_server.StartGameRequest.game_version",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="username",
            full_name="gfootball.eval_server.StartGameRequest.username",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="token",
            full_name="gfootball.eval_server.StartGameRequest.token",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="model_name",
            full_name="gfootball.eval_server.StartGameRequest.model_name",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="include_rendering",
            full_name="gfootball.eval_server.StartGameRequest.include_rendering",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=67,
    serialized_end=187,
)


_STARTGAMERESPONSE = _descriptor.Descriptor(
    name="StartGameResponse",
    full_name="gfootball.eval_server.StartGameResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="game_server_address",
            full_name="gfootball.eval_server.StartGameResponse.game_server_address",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="game_id",
            full_name="gfootball.eval_server.StartGameResponse.game_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=189,
    serialized_end=254,
)

DESCRIPTOR.message_types_by_name["StartGameRequest"] = _STARTGAMEREQUEST
DESCRIPTOR.message_types_by_name["StartGameResponse"] = _STARTGAMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartGameRequest = _reflection.GeneratedProtocolMessageType(
    "StartGameRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STARTGAMEREQUEST,
        "__module__": "gfootball.eval_server.proto.master_pb2"
        # @@protoc_insertion_point(class_scope:gfootball.eval_server.StartGameRequest)
    },
)
_sym_db.RegisterMessage(StartGameRequest)

StartGameResponse = _reflection.GeneratedProtocolMessageType(
    "StartGameResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STARTGAMERESPONSE,
        "__module__": "gfootball.eval_server.proto.master_pb2"
        # @@protoc_insertion_point(class_scope:gfootball.eval_server.StartGameResponse)
    },
)
_sym_db.RegisterMessage(StartGameResponse)


_MASTER = _descriptor.ServiceDescriptor(
    name="Master",
    full_name="gfootball.eval_server.Master",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=256,
    serialized_end=362,
    methods=[
        _descriptor.MethodDescriptor(
            name="StartGame",
            full_name="gfootball.eval_server.Master.StartGame",
            index=0,
            containing_service=None,
            input_type=_STARTGAMEREQUEST,
            output_type=_STARTGAMERESPONSE,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_MASTER)

DESCRIPTOR.services_by_name["Master"] = _MASTER

# @@protoc_insertion_point(module_scope)

#!/bin/bash
cd `dirname $0`
STRUCT_SRC_DIR=../proto/proto_data_struct
BASIC_DATA_INTERFACE_DIR=../proto/proto_data_interface
COMMON_TOOLS_DIR=../proto/proto_common_tools

STRUCT_OUTPUT_DIR=./proto_struct_py
BASIC_DATA_INTERFACE_OUTPUT=./proto_data_interface_py/
COMMON_TOOLS_OUTPUT=./proto_common_tools_py/

if [ ! -f $STRUCT_OUTPUT_DIR ]; then
   mkdir -pv $STRUCT_OUTPUT_DIR
   mkdir -pv $BASIC_DATA_INTERFACE_OUTPUT
   mkdir -pv $COMMON_TOOLS_OUTPUT
fi

for file in `ls $STRUCT_SRC_DIR|grep proto`
do
      python -m grpc.tools.protoc -I=$STRUCT_SRC_DIR --python_out=$STRUCT_OUTPUT_DIR $STRUCT_SRC_DIR/$file
done

if [ ! -f $BASIC_DATA_INTERFACE_OUTPUT ]; then
   mkdir -pv $BASIC_DATA_INTERFACE_OUTPUT
fi

echo "protobuf interface"
for file in `ls $BASIC_DATA_INTERFACE_DIR`
do
   python -m grpc.tools.protoc -I$BASIC_DATA_INTERFACE_DIR --python_out=$BASIC_DATA_INTERFACE_OUTPUT --grpc_python_out=$BASIC_DATA_INTERFACE_OUTPUT  $BASIC_DATA_INTERFACE_DIR/$file
done

for file in `ls $COMMON_TOOLS_DIR`
do
   python -m grpc.tools.protoc -I$COMMON_TOOLS_DIR --python_out=$COMMON_TOOLS_OUTPUT --grpc_python_out=$COMMON_TOOLS_OUTPUT $COMMON_TOOLS_DIR/$file
done

echo "# coding=utf-8" > $BASIC_DATA_INTERFACE_OUTPUT/__init__.py
echo "# coding=utf-8" > $STRUCT_OUTPUT_DIR/__init__.py
echo "# coding=utf-8" > $COMMON_TOOLS_OUTPUT/__init__.py


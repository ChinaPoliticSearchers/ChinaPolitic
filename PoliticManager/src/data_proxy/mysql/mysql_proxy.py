# coding=utf-8
# do bytes dynamic
from proto_data_interface_py import BasicDataManage_pb2


class BasicDataManage(BasicDataManage_pb2.DataServiceServicer):
    def Insert(self, InsertData, context):
        type_name = InsertData.insert_type_name
        insert_bytes = InsertData.insert_bytes
        insert_optionals = InsertData.insert_optionals
        from struct_proto_py.Event_pb2 import Event
        event = Event()
        event.ParseFromString(insert_bytes)
        print(event.event_name)
        data_response = BasicDataManage_pb2.DataResponse(success=True, response_type_name=InsertData.insert_type_name)
        return data_response

    def Update(self, UpdateData, context):
        pass

    def Query(self, QueryData, context):
        pass

    def Delete(self, DeleteData, context):
        pass

# coding=utf-8
# do bytes dynamic
from common_tools.reflection.struct_reflection import is_data_name_acceptable, get_instant_object
from proto_data_interface_py.BasicDataManage_pb2 import InsertData, DataResponse, Error, Level, DataServiceServicer,InsertOptional
from logging import Logger
import abc

from common_tools.generate_id import generator


class BasicDataManage(DataServiceServicer):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def return_not_acceptable_type(type_name):
        data_response = DataResponse(success=False, response_type_name=type_name,
                                     error=Error(message="{0} is not acceptable".format(type_name),
                                                 level=Level.Value("ERROR")))
        Logger.error("{0} is not acceptable".format(type_name))
        return data_response

    def Insert(self, insert_data, context):
        type_name = insert_data.insert_type_name
        insert_bytes = insert_data.insert_bytes
        insert_optionals = insert_data.insert_optionals

        if not is_data_name_acceptable(type_name):
            return self.return_not_acceptable_type(type_name)
        else:
            data_object = get_instant_object(data_name=type_name)
            data_object.ParseFromString(insert_bytes)
            # GenerateId use generator.py and provider the test
            if InsertOptional.Value("generate_id") in insert_optionals:
                data_object = generator.IdGeneratorMD5.generate_object(type_name, data_object)

            save_returns = self.save_detail(type_name=type_name, to_save_object=data_object,
                                            insert_optionals=insert_optionals)
            if not save_returns or (save_returns and len(save_returns) < 2):
                raise NotImplementedError("method save_detail must return if success and related message")
            success, message = save_returns[0], save_returns[1]
            if success:
                data_response = DataResponse(success=True, response_type_name=insert_data.insert_type_name)
                return data_response
            else:
                data_response = DataResponse(success=False, response_type_name=insert_data.insert_type_name,
                                             error=Error(message=message, level=Level.Value("ERROR")))
                return data_response

    def Update(self, UpdateData, context):
        pass

    def Query(self, QueryData, context):
        pass

    def Delete(self, DeleteData, context):
        pass

    @abc.abstractmethod
    def save_detail(self, type_name, to_save_object, insert_optionals):
        pass

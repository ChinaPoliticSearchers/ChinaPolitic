from common.basic_proxy import BasicDataManage


class MysqlDataManage(BasicDataManage):
    def save_detail(self, type_name, to_save_object, insert_optionals):
        print("I pretend I save")
        return True, "I pretend and i save"
import json

from marshmallow import EXCLUDE, pre_load, INCLUDE

from flask_frame.extension.marshmallow import ma
from module.user.model import User, Department


class BaseSchema():

    def load_external_id(self, value):
        return value.replace("{", "").replace("}", "")

    def convert_empty_array(self, value):
        if isinstance(value, list) and len(value) == 0:
            return None

        return value

    remark = ma.auto_field()


class UserSchema(ma.SQLAlchemyAutoSchema, BaseSchema):
    """
    用户
    """

    class Meta:
        model = User
        unknown = EXCLUDE
        load_instance = True

    loginid = ma.auto_field(data_key="sAMAccountName")
    name = ma.auto_field(data_key="name")
    email = ma.auto_field(data_key="mail")
    mobile_phone = ma.auto_field(data_key="mobile")
    external_id = ma.Method(data_key="objectGUID", deserialize="load_external_id")
    source = ma.auto_field(default="phfund")
    enable = ma.auto_field()

    @pre_load()
    def pre_load(self, in_data, **kwargs):
        for key in in_data.keys():
            in_data[key] = self.convert_empty_array(in_data.get(key))

        in_data["objectGUID"] = self.load_external_id(in_data["objectGUID"])
        in_data["department"] = [in_data["department"]] if in_data.get("department") else []
        in_data["enable"] = False if in_data.get("userStatus") and bin(in_data.get("userStatus"))[-2] == '1' else True
        in_data["remark"] = json.dumps(in_data, ensure_ascii=False)
        in_data["source"] = 'phfund'

        return in_data


class DepartmentSchema(ma.SQLAlchemySchema, BaseSchema):
    """
    部门
    """

    class Meta:
        model = Department
        unknown = EXCLUDE
        load_instance = True

    name = ma.auto_field(data_key="name")
    external_id = ma.Method(data_key="objectGUID", deserialize="load_external_id")
    source = ma.auto_field(default="phfund")
    order_no = ma.auto_field(data_key="description")

    @pre_load()
    def pre_load(self, in_data, **kwargs):
        for key in in_data.keys():
            in_data[key] = self.convert_empty_array(in_data.get(key))

        in_data["objectGUID"] = self.load_external_id(in_data["objectGUID"])

        in_data["remark"] = json.dumps(in_data, ensure_ascii=False)
        in_data["source"] = 'phfund'
        in_data["description"] = int(in_data["description"][0]) if in_data.get("description") and len(
            in_data.get("description")) > 0 else None

        return in_data


class PhfundUserSchema(ma.SQLAlchemySchema):
    """
    asr 请求参数
    """

    class Meta:
        model = User
        unknown = INCLUDE

    id = ma.auto_field(data_key="userId")
    loginid = ma.auto_field(data_key="username")
    name = ma.auto_field(data_key="realname")
    email = ma.auto_field()
    mobile_phone = ma.auto_field(data_key="mobilePhone")
    department_key = ma.auto_field(data_key="department")
    enable = ma.auto_field()

    @pre_load(pass_many=False)
    def pre_load(self, in_data, **kwargs):
        in_data["department"] = [in_data["department"]] if in_data.get("department") else []
        in_data["enable"] = True if in_data.get("userStatus") == "正常" else False

        return in_data

import json

from marshmallow import EXCLUDE, pre_load

from extension.marshmallow import ma
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

    @pre_load()
    def pre_load(self, in_data, **kwargs):
        for key in in_data.keys():
            in_data[key] = self.convert_empty_array(in_data.get(key))

        in_data["objectGUID"] = self.load_external_id(in_data["objectGUID"])
        in_data["department"] = [in_data["department"]] if in_data.get("department") else []
        in_data["userStatus"] = 0 if in_data.get("userStatus") == 514 else 1
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

    name = ma.auto_field(data_key="displayName")
    external_id = ma.Method(data_key="objectGUID", deserialize="load_external_id")
    source = ma.auto_field(default="phfund")

    @pre_load()
    def pre_load(self, in_data, **kwargs):
        for key in in_data.keys():
            in_data[key] = self.convert_empty_array(in_data.get(key))

        in_data["objectGUID"] = self.load_external_id(in_data["objectGUID"])

        in_data["remark"] = json.dumps(in_data, ensure_ascii=False)
        in_data["source"] = 'phfund'

        return in_data

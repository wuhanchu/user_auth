from marshmallow import INCLUDE, pre_load

from extension.marshmallow import ma
from module.user.model import User


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
    enabled = ma.auto_field(data_key="userStatus")

    @pre_load(pass_many=False)
    def pre_load(self, in_data, **kwargs):
        in_data["department"] = [in_data["department"]] if in_data.get("department") else []
        in_data["userStatus"] = 1 if in_data.get("userStatus") == "正常" else 0

        return in_data

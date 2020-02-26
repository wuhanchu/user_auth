# -*- coding: UTF-8 -*-
import base64
import os

from flask import Blueprint, request

from frame import register_tool
from frame.JsonResult import JsonResult

blueprint = Blueprint('license', __name__, url_prefix='/license')


@blueprint.route('', methods=['POST'])
def license_upload():
    """
     证书控制 - 上传证书文件
    :return:
    """
    licfile = request.files.get("license")
    license = licfile.read()
    licfile.close()
    info = base64.b64decode(license)
    is_allow, info = register_tool.check_license(info)
    if is_allow:
        with open("./license", "wb") as f:
            f.write(license)
        return JsonResult.success("注册成功")
    else:
        return JsonResult.error("注册失败，%s" % info)


@blueprint.route('', methods=['GET'])
def license_info():
    """
     查看证书信息
    :return:
    """
    # 判断证书是否存在，如果存在就返回有效时间
    if os.path.exists("./license"):
        with open("./license") as lic:
            lic_info = lic.read()
            lic_info = base64.b64decode(lic_info)
            is_enable, msg = register_tool.check_license(lic_info)
            if is_enable:
                return JsonResult.success("证书有效！", dict(msg,
                                                        machineInfo=register_tool.get_machineInfo()))
            else:
                res = {
                    "machineInfo": register_tool.get_machineInfo(),
                }
                return JsonResult.error("%s ，请联系相关销售进行申请证书！" % msg, res)

    else:
        res = {
            "machineInfo": register_tool.get_machineInfo()
        }
        return JsonResult.error("证书不存在，请联系相关销售进行申请证书！", res)


@blueprint.route('/check', methods=['get'])
def license_check():
    """
    证书验证
    :return:
    """
    if not register_tool.check_licfile():
        return '证书无效，请联系管理员更新!', 403
    return "证书有效"


def init_app(app, **kwargs):
    app.register_blueprint(blueprint)

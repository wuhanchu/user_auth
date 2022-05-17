# -*- coding: UTF-8 -*-
from http import HTTPStatus

from flask import request, abort

from flask_frame.extension.database import db
from flask_frame.api.response import Response
from flask_frame.util.db import auto_commit
from module.license.util import create_license
from . import blueprint, util
from .model import License

from module.auth.extension.oauth2 import require_oauth


@blueprint.route("", methods=["GET"])
def license_info():
    """
     查看证书信息
    :return:
    """
    product_key = request.args.get("product_key")

    record = None
    if product_key:
        record = License.query.filter_by(product_key=product_key).all()
    else:
        record = License.query.all()

    # 判断证书是否存在，如果存在就返回有效时间
    result = {"register_info": util.get_machine_info(), "license": []}
    
    for item in record:
        avaiable, recrod, message = util.check_license(item.content)
        result["license"].append({**recrod, "avaiable": avaiable, "message": message})

    # 返回
    return Response(True, data=result).mark_flask_response()


@blueprint.route("/check", methods=["get"])
def license_check():
    """
    证书验证
    :return:
    """
    product_key = request.args.get("product_key")
    record = License.query.get(product_key)
    if not record:
        return Response(
            False,  message="证书不存在，请联系管理员更新!", http_status=HTTPStatus.UNAUTHORIZED
        ).mark_flask_response()
          
    avaiable, recrod, message = util.check_license(record.content)
    if not record or not avaiable:
        return Response(
            False, data=recrod, message=message, http_status=HTTPStatus.UNAUTHORIZED
        ).mark_flask_response()

    return Response(
        data=recrod,
        message="证书有效!",
    ).mark_flask_response()


@blueprint.route("", methods=["POST"])
@auto_commit(db.session)
def license_upload():
    """
     证书控制 - 上传证书文件
    :return:
    """
    content = request.json.get("license")

    record_list = content.split("|")
    for item in record_list:
        is_allow, info, message = util.check_license(item)
        if is_allow:
            record = License(product_key=info["product_key"], content=item)
            db.session.merge(record)
        else:
            db.session.rollback()
            return Response(False, message="注册失败: %s" % message).mark_flask_response()

    # 成功
    return Response(message="注册成功").mark_flask_response()


@blueprint.route("/file", methods=["POST"])
def license_create():
    """
    证书创建
    :return: 证书编码
    """
    result = []
    params = request.json
    product_list = params.get("product")
    for product in product_list:
        license = create_license(
                params.get("register_info"),
                product.get("product_key"),
                product.get("due_time"),
                params.get("custom_name"),
            )
        result.append(license)

    # 返回
    return Response(data={"license":"|".join(result)}).mark_flask_response()

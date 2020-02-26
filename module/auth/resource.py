# -*- coding: UTF-8 -*-
import base64
import os

from authlib.integrations.flask_oauth2 import current_token
from authlib.oauth2 import OAuth2Error
from flask import render_template, redirect, jsonify
from flask import request, session
from werkzeug.security import gen_salt

from frame import JsonResult as js, register_tool
from frame.JsonResult import JsonResult
from module.auth.extension.oauth2 import authorization, require_oauth
from . import blueprint
from .model import *
from .model import OAuth2Client
from ..user.model import SysUser


@blueprint.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        user = SysUser.query.filter_by(loginid=username).first()
        session['id'] = user.id
        return redirect('/oauth')
    user = current_user()
    if user:
        clients = OAuth2Client.query.filter_by(user_id=user.id).all()
    else:
        clients = []
    return render_template('oauth_index.html', user=user, clients=clients)


@blueprint.route('/logout')
def logout():
    del session['id']
    return redirect('/')


@blueprint.route('/create_client', methods=('GET', 'POST'))
def create_client():
    user = current_user()
    if not user:
        return redirect('/')
    if request.method == 'GET':
        return render_template('create_client.html')
    client = OAuth2Client(**request.form.to_dict(flat=True))
    client.user_id = user.id
    client.client_id = gen_salt(24)
    if client.token_endpoint_auth_method == 'none':
        client.client_secret = ''
    else:
        client.client_secret = gen_salt(48)
    db.session.add(client)
    db.session.commit()
    return redirect('/')


@blueprint.route('/authorize', methods=['GET', 'POST'])
def authorize():
    user = current_user()
    if request.method == 'GET':
        try:
            grant = authorization.validate_consent_request(end_user=user)
        except OAuth2Error as error:
            return error.error
        return render_template('authorize.html', user=user, grant=grant)
    if not user and 'username' in request.form:
        username = request.form.get('username')
        user = SysUser.query.filter_by(loginid=username).first()
    if request.form['confirm']:
        grant_user = user
    else:
        grant_user = None
    return authorization.create_authorization_response(grant_user=grant_user)


@blueprint.route('/token', methods=['POST'])
def issue_token():
    res = authorization.create_token_response(request)
    return res


@blueprint.route('/revoke', methods=['POST'])
def revoke_token():
    return authorization.create_endpoint_response('revocation', request)


@blueprint.route('/current_user', methods=['GET'])
@require_oauth('profile')
def current_user():
    if current_token:
        user = current_token.user
        user = js.queryToDict(user)
        user.pop("password")
        user.pop("del_fg")
        user.pop("token")
        sql = """
            select p.name,p.url,p.method,p.key ,string_agg(cast(r.id as text),',') as role_id,string_agg(r.name,',') as role_name from sys_permission p 
                join sys_permission_group_rel rel on rel.permission_id = p.id
								join sys_permission_group_role gr on gr.permission_group_id = rel.permission_group_id
								-- join sys_permission_role pr on p.id = pr.permission_id 
                join sys_role r on r.id = gr.role_id
                join sys_user_role ur on r.id = ur.role_id
            where ur.user_id = '%s'
            group by p.name,p.url,p.method,p.key
        """ % user["id"]

        res = db.session.execute(sql).fetchall()
        user["permissions"] = js.queryToDict(res)
        sql_group = """
                select grp.id,grp.group_name,grp.key from sys_permission_group grp 
                    join sys_permission_group_role grole on grp.id = grole.permission_group_id 
                    join sys_role r on r.id = grole.role_id
                    join sys_user_role ur on r.id = ur.role_id
                where ur.user_id = '%s'
                """ % user["id"]
        res_group = db.session.execute(sql_group).fetchall()
        user["permission_groups"] = js.queryToDict(res_group)
        return jsonify(user)
    else:
        return JsonResult.error()


# 证书控制 - 上传证书文件
@blueprint.route('/register/file', methods=['POST'])
def license_upload():
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


# 证书控制 - 查看证书信息
@blueprint.route('/register/license', methods=['GET'])
def license_info():
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


@blueprint.route('/license/check', methods=['get'])
def license_check():
    # 证书验证
    if not register_tool.check_licfile():
        return '证书无效，请联系管理员更新!', 403
    return "证书有效"

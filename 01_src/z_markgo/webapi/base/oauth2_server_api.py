from flask import Blueprint, request, session
from flask import render_template, redirect, jsonify
from werkzeug.security import gen_salt
from authlib.flask.oauth2 import current_token
from authlib.oauth2 import OAuth2Error
from dao.models import db
from dao.model_user import *
from dao.model_oauth import OAuth2Client
from lib.oauth2 import authorization, require_oauth
from lib.JsonResult import JsonResult
from lib import JsonResult as js
from webapi import oauth_server

@oauth_server.route('/', methods=('GET', 'POST'))
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


@oauth_server.route('/logout')
def logout():
    del session['id']
    return redirect('/')


@oauth_server.route('/create_client', methods=('GET', 'POST'))
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


@oauth_server.route('/authorize', methods=['GET', 'POST'])
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


@oauth_server.route('/token', methods=['POST'])
def issue_token():
    res = authorization.create_token_response(request)
    return res


@oauth_server.route('/revoke', methods=['POST'])
def revoke_token():
    return authorization.create_endpoint_response('revocation',request)

@oauth_server.route('/current_user', methods=['GET'])
@require_oauth('profile')
def current_user():
    if current_token:
        user = current_token.user
        user = js.queryToDict(user)
        user.pop("password")
        user.pop("del_fg")
        user.pop("token")
        sql = """
            select p.name,p.url,p.method,p.key ,group_concat(r.id) as role_id,group_concat(r.name) as role_name from sys_permission p 
                join sys_permission_role pr on p.id = pr.permission_id 
                join sys_role r on r.id = pr.role_id
                join sys_user_role ur on r.id = ur.role_id
            where ur.user_id = '%s'
            group by p.name,p.url,p.method,p.key
        """%user["id"]

        res = db.session.execute(sql).fetchall()
        user["permissions"] = js.queryToDict(res)
        return JsonResult.success("查询成功",user)
    else:
        return JsonResult.error()
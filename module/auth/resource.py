# -*- coding: UTF-8 -*-
import json
import urllib.parse

import requests
from authlib.oauth2 import OAuth2Error
from flask import render_template, redirect, jsonify
from flask import request, session
from werkzeug.security import gen_salt

from config import ConfigDefine
from frame.http.response import Response
from frame.util import param_tool
from run import app
from . import blueprint
from .model import *
from .model import OAuth2Client
from .schema import client_param, client_res
from .. import get_user_pattern, blueprint_main
from ..user.model import User
from ..user.schema import PhfundUserSchema


@blueprint.route('/', methods=('GET', 'POST'))
def home():
    from ..user.resource import current_user

    if request.method == 'POST':
        username = request.form.get('username')
        user = User.query.filter_by(loginid=username).first()
        if user:
            session['id'] = user.id
        return redirect('/oauth')
    user = current_user()
    if user:
        clients = OAuth2Client.query.filter_by(user_id=user.id).all()
    else:
        clients = []
    return render_template('oauth_index.html', user=user, clients=clients)


@blueprint.route('/authorize', methods=['GET', 'POST'])
def authorize():
    from ..user.resource import current_user
    from module.auth.extension.oauth2 import authorization

    user = current_user()
    if request.method == 'GET':
        try:
            grant = authorization.validate_consent_request(end_user=user)
        except OAuth2Error as error:
            return error.error
        return render_template('authorize.html', user=user, grant=grant)
    if not user and 'username' in request.form:
        username = request.form.get('username')
        user = User.query.filter_by(loginid=username).first()
    if request.form['confirm']:
        grant_user = user
    else:
        grant_user = None
    return authorization.create_authorization_response(grant_user=grant_user)


@blueprint.route('/token', methods=['POST'])
def issue_token():
    from module.auth.extension.oauth2 import authorization

    res = authorization.create_token_response(request)
    return res


@blueprint.route('/revoke', methods=['POST'])
def revoke_token():
    from module.auth.extension.oauth2 import authorization

    return authorization.create_endpoint_response('revocation', request)


# 鹏华
if get_user_pattern() == ConfigDefine.UserPattern.phfund:

    @blueprint.route('/token', methods=('DELETE',))
    def logout():
        from flask import current_app, request

        url = urllib.parse.urljoin(
            current_app.config.get(ConfigDefine.USER_SERVER_URL),
            "/authentication/revoke_token")
        response = requests.get(url, headers=request.headers)
        result = response.json()
        if result.get("httpcode"):
            return result.get("message"), result.get("httpcode")

        result = PhfundUserSchema().loads(response.json())
        return jsonify(result)

# 默认
else:

    @blueprint.route('/token', methods=('DELETE',))
    @blueprint.route('/logout')
    def logout():
        del session['id']
        return redirect('/')


@blueprint_main.route('/oauth2_client', methods=['POST'])
def create_client():
    from .schema import OAuth2ClientSchema

    param = client_param.load(request.json)
    client = OAuth2Client(**param)
    client.client_id = gen_salt(24)

    if client.token_endpoint_auth_method == 'none':
        client.client_secret = ''
    else:
        client.client_secret = gen_salt(48)

    client.meta_data = {
        "scope": client.scope,
        "grant_types": json.loads(client.grant_type),
        "response_types": client.response_type
    }

    db.session.add(client)
    db.session.commit()

    return Response(data=client_res.dump(client)).get_response()

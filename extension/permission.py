from http import HTTPStatus

from flask import abort, g, request

app = None

# 配置参数
check_api = True  # 检查API权限
fetch_user = True  # 是否获取用户


def fetch_current_user(token_string):
    """
    todo 使用缓存
    获取当前用户
    :param token_string:
    :return:
    """
    global app

    from authlib.integrations.flask_oauth2 import current_token

    user = None
    if current_token:
        if current_token.user:
            from module.user.service import get_user_extend_info

            user = get_user_extend_info(current_token.user)
        else:
            user = {"client_id": current_token.client_id}
        g.current_user = user
    return user


def check_user_permission(token_string=None):
    """
    check current token
    :param token_string:
    :return:
    """
    # 获取token 不需要检查权限
    if request.url_rule.rule == "/auth/token":
        return True

    from module.auth.extension.oauth2 import require_oauth
    from flask_frame.extension.permission import check_url_permission

    @require_oauth()
    def local_oauth():
        pass

    local_oauth()

    user = fetch_current_user(token_string)
    return check_url_permission(user)


def init_app(flask_app):
    global app, check_api, fetch_user, get_user_extend_info

    app = flask_app
    check_api = app.config.get("CHECK_API", True)
    fetch_user = app.config.get("FETCH_USER", True)

    @app.before_request
    def app_proxy():
        # check permission
        token_string = request.headers.environ.get("HTTP_AUTHORIZATION")
        token_string = token_string.split(" ")[1] if token_string else None
        if fetch_user and not check_user_permission(token_string):
            if check_api:
                abort(HTTPStatus.UNAUTHORIZED, {"message": "API未授权"})

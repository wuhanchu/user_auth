from lib.models import *
from lib import JsonResult
import logging
from webapi import app
from lib.model_oauth import *

logger = logging.getLogger('flask.app')
#判断项目下是否有标注数据
def user_mark_count(project_id ,user_id=None):
    q = MarkProjectItem.query.filter_by(project_id=project_id)
    if user_id:
        q = q.filter_by(user_id = user_id)
    num = q.count()
    return num


#查询所有未加载的
def get_asr_items(project_id):
    q = MarkProjectItem.query.filter_by(project_id=project_id).filter(MarkProjectItem.asr_txt is not None)
    list = q.all()
    list = JsonResult.queryToDict(list)
    return list

#查询所有未加载的
def get_all_asr_items():
    dict = []
    list = MarkProject.query.filter(status=0).fiter(type='asr').all()
    for proj in list:
        items = get_asr_items(proj.id)
        if len(items)>0 :
            dict[proj] = items
    return dict
# 更新asr 解析结果
def update_asr_txt(res):
    with app.app_context():
        item_id = res._result[0]
        asr_txt  = res._result[1]
        if asr_txt :
            # 更新到数据库
            item_model = MarkProjectItem.query.get(item_id)
            item_model.asr_txt = asr_txt
            db.session.commit()

# 获取项目人员名单
def get_project_users(project_id):
    q = db.session.query(MarkProjectUser.user_id,MarkProjectUser.mark_role)
    q = q.filter(MarkProjectUser.project_id == project_id)
    return q.all()


def get_user_by_token(authorization):
    authorization = authorization.split(" ")
    if len(authorization) == 2:
        access_token = authorization[1]
        q = SysUser.query.join(OAuth2Token, OAuth2Token.user_id == SysUser.id).filter(
            OAuth2Token.access_token == access_token).filter(OAuth2Token.revoked == 0)
        user = q.first()
        if user:
            user = JsonResult.queryToDict(user)
            user.pop("password")
            user.pop("del_fg")
            user.pop("token")
            return user

if __name__ == '__main__':
    print(len(range(1,100,3)))
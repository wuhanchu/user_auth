from lib.models import *
from lib import JsonResult
import logging
from webapi import app
from lib.model_oauth import *

logger = logging.getLogger('flask.app')
# 判断项目下是否有标注数据


def user_mark_count(project_id, user_id=None):
    q = MarkProjectItem.query.filter_by(project_id=project_id)
    if user_id:
        q = q.filter_by(user_id=user_id)
    num = q.count()
    return num

# 查询所有未加载的


def get_asr_items(project_id):
    q = MarkProjectItem.query.filter_by(project_id=project_id).filter(
        MarkProjectItem.asr_txt.is_(None))
    list = q.all()
    list = JsonResult.queryToDict(list)
    return list

# 查询所有未加载的


def get_all_asr_items():
    dict = []
    list = MarkProject.query.filter(status=0).fiter(type='asr').all()
    for proj in list:
        items = get_asr_items(proj.id)
        if len(items) > 0:
            dict[proj] = items
    return dict

# 更新asr 解析结果


def update_asr_txt(res):
    if not res or not res._result[0] or not res._result[1]:
        return

    app.logger.info("update_asr_txt res" + str(res))
    with app.app_context():

        item_id = res._result[0]
        asr_txt = res._result[1]
        if asr_txt:
            # 更新到数据库
            item_model = MarkProjectItem.query.get(item_id)
            item_model.asr_txt = asr_txt
            db.session.commit()

# 获取已存储的item文件路径


def get_item_paths(project_id):

    filepaths = []
    res = MarkProjectItem.query.filter_by(project_id=project_id).all()
    for item in res:
        filepaths.append(item.filepath)
    return filepaths


# 获取项目人员名单
def get_project_users(project_id):
    q = db.session.query(MarkProjectUser.user_id, MarkProjectUser.mark_role)
    q = q.filter(MarkProjectUser.project_id == project_id)
    return q.all()


if __name__ == '__main__':
    print(len(range(1, 100, 3)))

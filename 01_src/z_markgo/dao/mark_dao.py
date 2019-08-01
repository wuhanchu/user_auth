from lib.models import *

#判断项目下是否有标注数据
def user_mark_count(project_id ,user_id=None):
    q = MarkProjectItem.query.filter_by(project_id=project_id)
    if user_id:
        q = q.filter_by(user_id = user_id)
    num = q.count()
    return num
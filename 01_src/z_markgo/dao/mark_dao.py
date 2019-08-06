from lib.models import *

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
    return q.all()

#查询所有未加载的
def get_all_asr_items():
    dict = []
    list = MarkProject.query.filter(status=0).fiter(type='asr').all()
    for proj in list:
        items = get_asr_items(proj.id)
        if len(items)>0 :
            dict[proj] = items
    return dict
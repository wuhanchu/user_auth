# -*- coding:utf-8 -*-
import os
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool,com_tool,sql_tool,busi_tool
from webapi import markRoute
from dao import mark_dao
from lib.oauth2 import require_oauth


item_root_path = busi_tool.get_item_root_path()
# 列表
@markRoute.route('/projects', methods=['GET'])
@require_oauth('profile')
def projects_list():
    sql =r"""select p.id,p.name,p.status,p.model_txt,p.ai_service,p.type,p.plan_time,p.inspection_persent,p.create_time,p.remarks
        ,p.asr_score,p.frame_rate,pu.sum_user,pi.sum_items,pi.sum_mark_items from mark_project p join
        (SELECT p.id pid,count(pu.project_id) as sum_user FROM mark_project p left join mark_project_user pu on pu.project_id  = p.id
        group by p.id) pu on pu.pid = p.id join
        (select p.id pid,count(pi.id) sum_items,sum(case when pi.status=1 and pi.inspection_status !=2  then 1 else 0 end) 
        sum_mark_items from mark_project p left join mark_project_items pi on pi.project_id  = p.id group by p.id) 
        pi on pi.pid = p.id where 1=1 """

    name = request.args.get("name")
    type = request.args.get("type")
    if name is not None and name != '':
        sql = sql + " and p.name like '%" + name + "%'"
    if type is not None  and type != '':
        sql = sql + " and p.type = '" + type + "'"

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if param_tool.str_is_empty(sort):
        sort = "-id"
    res,total = sql_tool.mysql_page(db,sql,offset,limit,sort)
    return JsonResult.res_page(res,total)

# 详细信息
@markRoute.route('/projects/<id>', methods=['GET'])
@require_oauth('profile')
def get_info(id):
    obj = MarkProject.query.get(id)
    return JsonResult.queryResult(obj)

#添加
@markRoute.route('/projects', methods=['POST'])
@require_oauth('profile')
def projects_add():
    obj = MarkProject()
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    obj.create_time = com_tool.get_curr_date()
    db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"userid": obj.id})

# 更新
@markRoute.route('/projects/<id>', methods=['PUT','PATCH'])
@require_oauth('profile')
def projects_update(id):
    obj = MarkProject.query.get(id)
    #todo 判断是否可以修改type（标注类型）
    if obj is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    #将参数加载进去
    param_tool.set_dict_parm(obj,args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": obj.id})

#删除
@markRoute.route('/projects/<id>', methods=['DELETE'])
@require_oauth('profile')
def projects_delete(id):
    obj = MarkProject.query.get(id)

    # 判断是否有标注数据
    if mark_dao.user_mark_count(id) > 0:
        return JsonResult.error("该项目已经上传标注数据！请先删除标注数据！")

    # 删除项目用户分配信息
    users = MarkProjectUser.query.filter_by(project_id=id).delete(synchronize_session=False)

    db.session.delete(obj)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})

@markRoute.route('/projects/<id>/project_pkg', methods=['GET'])
@require_oauth('profile')
def export_project(id):
    # 导出打包文件
    list = MarkProjectItem.query.filter_by(project_id = id)
    dir_path = os.path.join(item_root_path, id)
    project = MarkProject.query.get(id)
    txt_file = os.path.join(dir_path,"%s_标注文本.txt"%(project.name))
    with open(txt_file, 'w') as f:
        for item in list:
            str = "%s %s\n"%(item.filepath,com_tool.if_null(item.inspection_txt,item.mark_txt))
            f.write(str)
    zip_file = os.path.join(item_root_path,"%s(%s)_标注信息.zip"%(project.name,project.id))
    com_tool.zip_dir(dir_path,zip_file)
    return send_file(zip_file)
# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool,com_tool
from webapi import markRoute
import os


item_root_path = '../mark_items'
if not os.path.exists(item_root_path):
    os.makedirs(item_root_path)

# 列表
@markRoute.route('/projects', methods=['GET'])
def list():
    q = MarkProject.query
    name = request.args.get("name")
    type = request.args.get("type")
    if name is not None and name != '':
        q = q.filter(MarkProject.name.like("%" + name + "%"))
    if type is not None  and type != '':
        q = q.filter_by(type = type)
    q = q.order_by(MarkProject.name.desc())

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    page = int(offset / limit) + 1
    if page == 0 : page = 1
    page = q.paginate(page=page, per_page=limit)
    return JsonResult.page(page)

# 详细信息
@markRoute.route('/projects/<id>', methods=['GET'])
def get_info(id):
    obj = MarkProject.query.get(id)
    return JsonResult.queryResult(obj)

#导入文件
@markRoute.route('/projects_item/upload', methods=['POST'])
def upload_item():
    project_id = request.form.get("project_id")
    item_file = request.files.get("item_file")

    # 创建item项目目录
    item_path = os.path.join(item_root_path,project_id)
    if not os.path.exists(item_path):
        os.makedirs(item_path)
    # 保存文件
    item_file.save(item_path)
    # 解压文件

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
def update(id):
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
def delete(id):
    obj = MarkProject.query.get(id)
    db.session.delete(obj)
    #todo 判断是否有标注数据
    #todo 删除项目用户分配信息
    # sql = """ delete from ts_meetasr_log where meetid='%s' """ % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})
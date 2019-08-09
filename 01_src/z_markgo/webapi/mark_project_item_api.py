# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool,com_tool,sql_tool,busi_tool,asr_tool
from lib.dk_thread_pool import dk_thread_pool
from webapi import markRoute,app
from dao import mark_dao
import os
from sqlalchemy.orm import aliased

item_root_path = busi_tool.get_item_root_path()
print(item_root_path )
if not os.path.exists(item_root_path):
    os.makedirs(item_root_path)

# 列表
@markRoute.route('/project_items', methods=['GET'])
def project_items_list():
    project_id = request.args.get("project_id")
    filepath = request.args.get("filepath")
    status = request.args.get("status")
    user_id = request.args.get("user_id")

    InspectionPerson = aliased(SysUser)
    q = db.session.query(MarkProjectItem.id,MarkProjectItem.project_id,MarkProjectItem.filepath,MarkProjectItem.status,MarkProjectItem.asr_txt,
        MarkProjectItem.mark_txt,MarkProjectItem.user_id,MarkProjectItem.inspection_status,MarkProjectItem.mark_time,MarkProjectItem.assigned_time
        ,MarkProjectItem.inspection_time,MarkProjectItem.inspection_person,SysUser.name.label("mark_person_name"),InspectionPerson.name.label("inspection_person_name")
        ).outerjoin(SysUser, MarkProjectItem.user)\
        .outerjoin(InspectionPerson,MarkProjectItem.sys_user)

    q = q.filter(MarkProjectItem.project_id == project_id)

    if filepath is not None and filepath != '':
        q = q.filter(MarkProjectItem.filepath.like("%" + filepath + "%"))
    if status is not None  and status != '':
        q = q.filter(MarkProjectItem.status == status)
    q = q.order_by(MarkProjectItem.status)

    if user_id is not None  and user_id != '':
        q = q.filter(MarkProjectItem.user_id == user_id)

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    list,total = sql_tool.model_page(q,limit,offset)
    return JsonResult.res_page(list,total)

# 详细信息
@markRoute.route('/project_items/<id>', methods=['GET'])
def project_items_get_info(id):
    obj = MarkProjectItem.query.get(id)
    return JsonResult.queryResult(obj)

#导入文件
@markRoute.route('/project_items/upload', methods=['POST'])
def project_items_upload():
    project_id = request.form.get("project_id")
    zip_file = request.files.get("item_file")

    # 创建item项目目录
    item_path = os.path.join(item_root_path,project_id)
    if not os.path.exists(item_path):
        os.makedirs(item_path)
    # 保存文件
    zip_file_path = os.path.join(item_path,zip_file.filename)
    zip_file.save(zip_file_path)
    zip_file.close()
    # 解压文件
    com_tool.unzip_file(zip_file_path,item_path)
    #删除压缩文件
    os.remove(zip_file_path)
    #遍历文件
    item_paths = com_tool.enum_path_files(item_path)
    path_len = len(item_root_path)+1
    #创建item条目
    for project_item_path in item_paths:
        item = MarkProjectItem(project_id = project_id,filepath = project_item_path[path_len:])
        db.session.add(item)
    db.session.commit()
    #判断是否要进行文本解析，如果需要就调用后台任务
    project = MarkProject.query.get(project_id)
    if project.type == "asr":
        ai_service = AiService.query.get(project.ai_service)
        items = mark_dao.get_asr_items(project_id)
        for item in items:
            filepath = os.path.join(item_root_path, item["filepath"])
            dk_thread_pool.submit(busi_tool.tc_asr,mark_dao.update_asr_txt,item["id"],ai_service.service_url,filepath)

    return JsonResult.success("导入音频成功！总条数%s"%len(item_paths))

# 更新
@markRoute.route('/project_items/<id>', methods=['PUT','PATCH'])
def project_items_update(id):
    obj = MarkProjectItem.query.get(id)
    if obj is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    if args["mark_txt"] != None  :
        obj.mark_time = param_tool.get_curr_time()
    if args["inspection_status"] != None :
        obj.inspection_time = param_tool.get_curr_time()

    db.session.commit()
    return JsonResult.success("更新成功！",{"id": obj.id})

#删除
@markRoute.route('/project_items/<id>', methods=['DELETE'])
def project_items_delete(id):
    obj = MarkProjectItem.query.get(id)
    if obj is None:
        return JsonResult.error("对象不存在！", {"id": id})
    path = os.path.join(item_root_path,obj.filepath)
    os.remove(path)
    db.session.delete(obj)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})

#批量删除
@markRoute.route('/project_items', methods=['DELETE'])
def project_items_delete_batch():
    args = request.args
    ids = args.get("ids").split(',');

    objs = MarkProjectItem.query.filter(MarkProjectItem.id.in_(ids)).all()
    for obj in objs:
        path = os.path.join(item_root_path, obj.filepath)
        try:
            os.remove(path)
        except:
            app.logger.warn("文件没找到：%s"%path)
        db.session.delete(obj)

    db.session.commit()
    return JsonResult.success("批量删除成功！")

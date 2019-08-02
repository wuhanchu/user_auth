# -*- coding:utf-8 -*-
from flask import request, send_file,make_response,render_template
from lib.models import *
from lib.JsonResult import JsonResult
from lib import param_tool,com_tool,sql_tool
from webapi import markRoute,app
import os

work_dir = os.getcwd()
print(os.path.dirname(work_dir))
item_root_path = os.path.join(os.path.dirname(work_dir),"z_markgo_items")
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

    q = MarkProjectItem.query.filter_by(project_id=project_id)
    if filepath is not None and filepath != '':
        q = q.filter(MarkProjectItem.filepath.like("%" + filepath + "%"))
    if status is not None  and status != '':
        q = q.filter_by(status = status)
    q = q.order_by(MarkProjectItem.status)
    q.outerjoin(SysUser)
    if user_id is not None  and user_id != '':
        q = q.filter_by(user_id = user_id)

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    list,total = sql_tool.model_page(q,limit,offset)
    return JsonResult.res_page(list,total)

# 详细信息
@markRoute.route('/projects/<id>', methods=['GET'])
def project_items_get_info(id):
    obj = MarkProject.query.get(id)
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
    path_len = len(item_root_path)
    #创建item条目
    for project_item_path in item_paths:
        item = MarkProjectItem(project_id = project_id,filepath = project_item_path[path_len:])
        db.session.add(item)
    db.session.commit()
    #todo 判断是否要进行文本解析，如果需要就调用后台任务

    return JsonResult.success("导入音频成功！总条数%s"%len(item_paths) )

# 更新
@markRoute.route('/projects/<id>', methods=['PUT','PATCH'])
def project_items_update(id):
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
@markRoute.route('/project_items/del_batch', methods=['DELETE'])
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

#批量删除
@markRoute.route('/project_items/get_next_item', methods=['GET'])
def get_next_item():
    #todo 获取下一个标注文件，如果是机转的，应尽量取已经机转的文件
    return JsonResult.success("good")
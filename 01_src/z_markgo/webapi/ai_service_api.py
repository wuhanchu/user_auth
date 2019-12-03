# -*- coding:utf-8 -*-
from flask import request
from lib.models import AiService,db
from lib.JsonResult import JsonResult
from lib import com_tool, sql_tool, param_tool
from webapi import baseRoute
from lib.oauth2 import require_oauth

# 列表
@baseRoute.route('/aiservices', methods=['GET'])
@require_oauth('profile')
def aiservices_list():
    q = AiService.query
    name = request.args.get("name")
    type = request.args.get("type")
    if name is not None and name != '':
        q = q.filter(AiService.name.like("%" + name + "%"))
    if type is not None  and type != '':
        q = q.filter_by(type = type)
    # q = q.order_by(AiService.name.desc())

    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    sort = request.args.get('sort')
    if sort == None:
        sort = "-id"
    list, total = sql_tool.model_page(q,limit, offset,sort)
    return JsonResult.res_page(list, total)


# 详细信息
@baseRoute.route('/aiservices/<id>', methods=['GET'])
def aiservices_get_info(id):
    obj = AiService.query.get(id)
    return JsonResult.queryResult(obj)

#添加
@baseRoute.route('/aiservices', methods=['POST'])
def aiservices_add():
    obj = AiService()
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    obj.create_time = com_tool.get_curr_date()
    db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"userid": obj.id})

# 更新
@baseRoute.route('/aiservices/<id>', methods=['PUT','PATCH'])
def aiservices_update(id):
    obj = AiService.query.get(id)
    #todo 判断是否可以修改type（标注类型）
    if obj is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    #将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": obj.id})

#删除
@baseRoute.route('/aiservices/<id>', methods=['DELETE'])
def aiservices_delete(id):
    obj = AiService.query.get(id)
    db.session.delete(obj)
    #todo 判断是否有标注数据
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})



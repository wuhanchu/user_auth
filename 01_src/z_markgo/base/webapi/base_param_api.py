
from flask import request
from ..dao.base_model import *
from ..lib.JsonResult import JsonResult
from ..lib import param_tool
from . import baseRoute


# 列表
@baseRoute.route('/param', methods=['GET'])
def param_list():
    q = SysParam.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter(SysParam.name.like("%" + name + "%"))
    q = q.order_by(SysParam.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    page = int(offset / limit)
    if page == 0 : page = 1
    page = q.paginate(page=page, per_page=limit)
    return JsonResult.page(page)

# 详细信息
@baseRoute.route('/param/<id>', methods=['GET'])
def get_param(id):
    obj = SysParam.query.get(id)
    return JsonResult.queryResult(obj)

# 添加
@baseRoute.route('/param', methods=['POST'])
def add_param():
    obj = SysParam()
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"id": obj.id})

# 更新， PUT:全部字段 ；PATCH:部分字段
@baseRoute.route('/param/<id>', methods=['PUT','PATCH'])
def update_param(id):
    obj = SysParam.query.get(id)
    if obj is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    #将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": obj.id})

@baseRoute.route('/param/<id>', methods=['DELETE'])
def del_param(id):
    "删除"
    obj = SysParam.query.get(id)
    db.session.delete(obj)
    # sql = "delete from ts_meetasr_log where meetid='%s' " % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})



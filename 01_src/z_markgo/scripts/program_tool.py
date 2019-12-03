# 项目工具
import subprocess,os

model = """
from flask import request, send_file,make_response,render_template
from dao.models import *
from lib.JsonResult import JsonResult
from webapi import baseRoute,app

# 列表
@baseRoute.route('/{model_name}', methods=['GET'])
def {model_name}_list():
    q = {ModelName}.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter({ModelName}.name.like("%" + name + "%"))
    q = q.order_by({ModelName}.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    page = int(offset / limit)
    if page == 0 : page = 1
    page = q.paginate(page=page, per_page=limit)
    return JsonResult.page(page)

# 详细信息
@baseRoute.route('/{model_name}/<id>', methods=['GET'])
def get_{model_name}(id):
    obj = {ModelName}.query.get(id)
    return JsonResult.queryResult(obj)

# 添加
@baseRoute.route('/{model_name}', methods=['POST'])
def add_{model_name}():
    obj = {ModelName}()
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"id": obj.id})

# 更新， PUT:全部字段 ；PATCH:部分字段
@baseRoute.route('/{model_name}/<id>', methods=['PUT'])
def update_{model_name}(id):
    obj = {ModelName}.query.get(id)
    if obj is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    #将参数加载进去
    param_tool.set_dict_parm(obj,args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": obj.id})

@baseRoute.route('/{model_name}/<id>', methods=['DELETE'])
def del_{model_name}(id):
    "删除"
    obj = {ModelName}.query.get(id)
    db.session.delete(obj)
    # sql = "delete from ts_meetasr_log where meetid='%s' " % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})


"""

def auto_create_models(model_name,ModelName):
    # 自动生成对象的增删改查代码
    filepath = "../webapi/%s_api.py"%model_name
    #判断文件是否存在
    if os.path.exists(filepath):
        print("文件已存在，是否覆盖？（Yy/Nn）")
        reply = input()
        if reply != "Y" and reply != "y":
            print("文件已存在,不覆盖，退出！")
            return

    #替换参数
    new_model = model.replace("{model_name}",model_name)
    new_model = new_model.replace("{ModelName}",ModelName)
    #输出到文件
    with open(filepath, 'w',encoding="utf-8") as output:
        output.write(new_model)
        print("生成文件：%s"%filepath)


if __name__ == '__main__':
    auto_create_models('Permission_group','SysPermissionGroup')
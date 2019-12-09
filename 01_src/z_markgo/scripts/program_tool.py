# 项目工具
import subprocess,os,json

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
    if obj is None:
        return JsonResult.error("删除失败，id=%s不存在！"%record_id)
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


def get_eoapi(app):
    data = {
    "baseInfo": {
      "apiName": "",
      "apiURI": "",
      "apiProtocol": 0,
      "apiSuccessMock": "",
      "apiFailureMock": "",
      "apiRequestType": 0,
      "apiStatus": 0,
      "starred": 0,
      "createTime": "",
      "apiNoteType": 1,
      "apiNoteRaw": "",
      "apiNote": "",
      "apiRequestParamType": 0,
      "apiRequestRaw": "",
      "apiFailureStatusCode": "200",
      "apiSuccessStatusCode": "200",
      "apiFailureContentType": "text\/html; charset=UTF-8",
      "apiSuccessContentType": "text\/html; charset=UTF-8",
      "apiRequestParamJsonType": 0,
      "apiUpdateTime": "",
      "apiTag": "",
      "advancedSetting": {
        "requestRedirect": 1
      }
    },
    "headerInfo": [

    ],
    "authInfo": {
      "status": "0"
    },
    "requestInfo": [

    ],
    "urlParam": [

    ],
    "restfulParam": [

    ],
    "resultInfo": [

    ],
    "responseHeader": [

    ],
    "resultParamJsonType": 0,
    "resultParamType": 0,
    "structureID": "[]",
    "databaseFieldID": "[]",
    "globalStructureID": "[]",
    "testCastList": [

    ],
    "dataStructureList": [

    ],
    "globalDataStructureList": [

    ],
    "mockExpectationList": [

    ]
  }
    json_model = []
    is_exit = 0
    rules = app.url_map.iter_rules()
    for rule in rules:
        apiURI = rule.rule
        data['baseInfo']['apiURI'] = apiURI.replace("<", "{").replace(">", "}")
        for ele in rule.methods:
            if ele != 'HEAD' and ele != 'OPTIONS' and is_exit != 1:
                if ele=='GET':
                    data['baseInfo']['apiRequestType'] = 1
                elif ele == 'POST':
                    data['baseInfo']['apiRequestType'] = 0
                elif ele == 'PUT':
                    data['baseInfo']['apiRequestType'] = 2
                elif ele == 'DELETE':
                    data['baseInfo']['apiRequestType'] = 3
                json_model.append(json.dumps(data))
                is_exit = 1
        is_exit = 0
    with open('./api2eolinker.amsa', 'a', encoding='utf-8') as f:
        f.write('[')
        for i in range(len(json_model)):
            f.write(json_model[i])
            if i < len(json_model)-1:
                f.write(',')
        f.write(']')
        f.close()
    return ''


if __name__ == '__main__':
    auto_create_models('Permission_group','SysPermissionGroup')

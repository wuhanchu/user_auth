from flask import request
from dao.base_model import *
from dao.models import db
from lib.JsonResult import JsonResult
from lib import param_tool
from webapi import baseRoute,app
import json
from lib.oauth2 import require_oauth
# 权限列表
@baseRoute.route('/permissions', methods=['GET'])
@require_oauth("profile")
def permission_list():
    q = SysPermission.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter(SysPermission.name.like("%" + name + "%"))
    q = q.order_by(SysPermission.name.desc())
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    page = int(offset / limit)
    if page == 0 : page = 1
    page = q.paginate(page=page, per_page=limit)
    return JsonResult.page(page)

# 详细权限信息
@baseRoute.route('/permissions/<id>', methods=['GET'])
@require_oauth("profile")
def get_permission(id):
    permission = SysPermission.query.get(id)
    return JsonResult.queryResult(permission)

@baseRoute.route('/permissions', methods=['POST'])
@require_oauth("profile")
def add_permission():
    obj = SysPermission()
    args = request.get_json()
    # 将参数加载进去
    param_tool.set_dict_parm(obj, args)
    db.session.add(obj)
    db.session.commit()
    return JsonResult.success("创建成功！", {"permission_id": obj.id})

@baseRoute.route('/permissions/<id>', methods=['PUT','PATCH'])
@require_oauth("profile")
def update_permission(id):
    permission = SysPermission.query.get(id)
    if permission is None :
        return JsonResult.error("对象不存在，id=%s"%id)
    args = request.get_json()
    #将参数加载进去
    param_tool.set_dict_parm(permission, args)
    db.session.commit()
    return JsonResult.success("更新成功！",{"id": permission.id})

@baseRoute.route('/permissions/<id>', methods=['DELETE'])
@require_oauth("profile")
def del_permission(id):
    "删除权限"
    permission = SysPermission.query.get(id)
    db.session.delete(permission)
    # sql = """ delete from ts_meetasr_log where meetid='%s' """ % meetid
    # db.session.execute(sql)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})


@baseRoute.route('/permission_sql', methods=['GET'])
def permission_sql():
    str = ''
    is_exit = 0
    sql_list = []
    sql = 'insert into sys_permission(url,method) select \'%s\' as url,\'%s\' as method from dual WHERE NOT EXISTS (SELECT 1 FROM sys_permission WHERE url=\'%s\' and method=\'%s\' );\n'
    rules = app.url_map.iter_rules()
    for rule in rules:
        for ele in rule.methods:
            if ele!='HEAD' and ele!= 'OPTIONS' and is_exit!=1:
                if rule.rule.find("users")>0 and ele == "PUT" :
                    print(rule.rule)
                sql_list.append(sql%(rule.rule,ele,rule.rule,ele))
                is_exit = 1
        is_exit = 0
    for i in range(len(sql_list)-1):
        str+=sql_list[i]
    return str

@baseRoute.route('/permission_eoapi',methods=['GET'])
def permission_eoapi():
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
    with open('C:/Users/czc/Desktop/api2eolinker.json', 'w', encoding='utf-8') as f:
        f.write('[')
        for i in range(len(json_model)):
            f.write(json_model[i])
            if i < len(json_model)-1:
                f.write(',')
        f.write(']')
        f.close()
    return ''

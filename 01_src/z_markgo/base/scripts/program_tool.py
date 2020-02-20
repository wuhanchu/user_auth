# 项目工具
import subprocess, os, json,re
from dao.models import *
from dao.model_user import *
from webapi import app,DEFAULT_MODULES,base_api,call_robot_api,recording_api,task_api,txt_robot_api,talk_robot_api
from webapi.talk_flow import flow_node_api,intention_api,intention_answer_api,question_api,intention_pkg_api,intention_pkg_answer_api,question_group_api
model = """
from flask import request, send_file,make_response,render_template
from dao.models import *
from lib.JsonResult import JsonResult
from webapi import baseRoute,app
from lib import param_tool,sql_tool
from lib.oauth2 import require_oauth

# 列表
@baseRoute.route('/{model_name}', methods=['GET'])
@require_oauth("profile")
def {model_name}_list():
    q = {ModelName}.query
    name = request.args.get("name")
    if name is not None:
        q = q.filter({ModelName}.name.like("%" + name + "%"))
    q = q.order_by({ModelName}.id.desc())
    sort = request.args.get('sort')
    offset = int(request.args.get('offset'))
    limit = int(request.args.get('limit'))
    res, total = sql_tool.model_page(q, limit, offset, sort)
    return JsonResult.res_page(res, total)

# 详细信息
@baseRoute.route('/{model_name}/<id>', methods=['GET'])
@require_oauth("profile")
def get_{model_name}(id):
    obj = {ModelName}.query.get(id)
    return JsonResult.queryResult(obj)

# 添加
@baseRoute.route('/{model_name}', methods=['POST'])
@require_oauth("profile")
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
@require_oauth("profile")
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
@require_oauth("profile")
def del_{model_name}(id):
    "删除"
    obj = {ModelName}.query.get(id)
    if obj is None:
        return JsonResult.error("删除失败，id=%s不存在！"%id)
        
    db.session.delete(obj)
    db.session.commit()
    return JsonResult.success("删除成功！", {"id": id})


"""


def auto_create_models(model_name, ModelName):
    # 自动生成对象的增删改查代码
    filepath = "../webapi/%s_api.py" % model_name
    # 判断文件是否存在
    if os.path.exists(filepath):
        print("文件已存在，是否覆盖？（Yy/Nn）")
        reply = input()
        if reply != "Y" and reply != "y":
            print("文件已存在,不覆盖，退出！")
            return

    # 替换参数
    new_model = model.replace("{model_name}", model_name)
    new_model = new_model.replace("{ModelName}", ModelName)

    # 输出到文件
    with open(filepath, 'w', encoding="utf-8") as output:
        output.write(new_model)
        print("生成文件：%s" % filepath)

def setRequestInfo(obj):
    if obj is None:
        return []
    else:
        cols = []
        for col in obj._sa_instance_state._unloaded_non_object:
            if col == "id" :
                continue
            cols.append({"paramNotNull": "0","paramType": "0","paramName": col,"paramKey": col,"paramValue": "","paramLimit": "","paramNote": "","paramValueList": [],
                "default": 0,"childList": []
            })
        return cols

def setRestParam(params):
    objs = []
    for param in params:
        objs.append({
        "paramNotNull": "0",
        "paramType": "0",
        "paramName": param[1:-1],
        "paramKey": "",
        "paramValue": "",
        "paramLimit": "",
        "paramNote": "",
        "paramValueList": [],
        "default": 0
    })
    return []


def auto_create_eoapi(models):
    for module in DEFAULT_MODULES:
        print("Blueprint regist %s !" % module.name)
        app.register_blueprint(module)

    page_param = [{"paramNotNull":"0","paramType":"3","paramName":"每页条数","paramKey":"limit","paramValue":"10","paramLimit":"","paramNote":"","paramValueList":[],"default":0},
            {"paramNotNull":"0","paramType":"3","paramName":"起始行","paramKey":"offset","paramValue":"0","paramLimit":"","paramNote":"","paramValueList":[],"default":0},
            {"paramNotNull":"0","paramType":"0","paramName":"排序字段","paramKey":"sort","paramValue":"id","paramLimit":"","paramNote":"","paramValueList":[],"default":0}]
    json_model = []
    rules = app.url_map.iter_rules()
    for rule in rules:
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
                "apiRequestParamType": 2,
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
        apiURI = rule.rule
        model = None
        for x in models:
            if apiURI.find(x["id"])>0:
                model = x
                break
        if model== None :
            continue
        params =  re.findall(r"<.*>",apiURI)
        if len(params)>0:
            data['baseInfo']['apiURI'] = apiURI.replace("<", "{").replace(">", "}")
            data['restfulParam'] = setRestParam(params)
        else:
            data['baseInfo']['apiURI'] = apiURI
        is_exit = 0
        for ele in rule.methods:
            if ele != 'HEAD' and ele != 'OPTIONS' and is_exit != 1:
                if ele=='GET':
                    data['baseInfo']['apiRequestType'] = 1
                    if apiURI.find("<") > 0: # 有带id
                        data['baseInfo']['apiName'] = model["name"] + "_详情"
                    else:
                        data['baseInfo']['apiName'] = model["name"] + "_列表"
                        data['urlParam'] = page_param
                elif ele == 'POST':
                    data['baseInfo']['apiRequestType'] = 0
                    data['baseInfo']['apiName'] = model["name"] + "_添加"
                    data['requestInfo'] = setRequestInfo(model["object"])
                elif ele == 'PUT':
                    data['baseInfo']['apiRequestType'] = 2
                    data['baseInfo']['apiName'] = model["name"] + "_更新"
                    data['requestInfo'] = setRequestInfo(model["object"])
                elif ele == 'DELETE':
                    data['baseInfo']['apiRequestType'] = 3
                    data['baseInfo']['apiName'] = model["name"]+"_删除"
                json_model.append(json.dumps(data))
                is_exit = 1


    with open('./api2eolinker.amsa', 'w', encoding='utf-8') as f:
        f.write('[')
        for i in range(len(json_model)):
            f.write(json_model[i])
            if i < len(json_model) - 1:
                f.write(',')
        f.write(']')
        f.close()
    print("生成文件：api2eolinker.amsa")

# 自动生成权限导入sql
def auto_create_permission_sql():
    for module in DEFAULT_MODULES:
        print("Blueprint regist %s !" % module.name)
        app.register_blueprint(module)

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
    print(str)
    return str

if __name__ == '__main__':
    #生成 api 代码文件
    # auto_create_models('flow_node','TalkFlowNode')
    # auto_create_models('intention', 'NodeIntention')
    # auto_create_models('intention_answer', 'NodeIntentionAnswer')
    # auto_create_models('question', 'Question')
    # auto_create_models('question_group', 'QuestionGroup')
    # auto_create_models('intention_pkg', 'TalkIntentionPkg')
    # auto_create_models('intention_pkg_answer', 'TalkIntentionPkgAnswer')
    # auto_create_models('', 'TalkIntentionPkgAnswer')


    # 生成api接口文档
    # auto_create_eoapi([{"id":"/flow_node","name":"流程节点","object":TalkFlowNode()}])
    # auto_create_eoapi([{"id": "/intention", "name": "节点意图管理", "object": NodeIntention()}])
    # auto_create_eoapi([{"id": "/intention_answer", "name": "意图答复管理", "object": NodeIntentionAnswer()}])
    # auto_create_eoapi([{"id": "/question", "name": "问答库管理", "object": Question()}])
    # auto_create_eoapi([{"id": "/question_group", "name": "问答库分组管理", "object": QuestionGroup()}])
    # auto_create_eoapi([{"id": "/intention_pkg", "name": "意图库管理", "object": TalkIntentionPkg()}])
    # auto_create_eoapi([{"id": "/intention_pkg_answer", "name": "意图库答复管理", "object": TalkIntentionPkg()}])
    # auto_create_eoapi([{"id": "/intention_pkg_answer", "name": "意图库答复管理", "object": SysPa ()}])

    # 生成权限导入sql
    auto_create_permission_sql()
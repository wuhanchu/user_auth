from flask import jsonify
from datetime import datetime as cdatetime #有时候会返回datatime类型
from datetime import date,time
from flask_sqlalchemy import Model
from sqlalchemy import DateTime,Numeric,Date,Time #有时又是DateTime

# 返回结果： 成功code=100； 失败：code=-1
SUCCESS_CODE = 100
ERROR_CODE = -1
class JsonResult:

    def custom(code=None, msg=None, result=None):
        return jsonify({'code': code, 'msg': msg, 'result': None})

    def success(msg=None):
        return jsonify({'code': SUCCESS_CODE, 'msg': msg, 'result': None})

    def success(msg=None, result=None):
        return jsonify({'code': SUCCESS_CODE, 'msg': msg, 'result': result})

    def error(msg=None):
        return jsonify({'code': ERROR_CODE, 'msg': msg, 'result': None})

    def error(msg=None, result=None):
        return jsonify({'code': SUCCESS_CODE, 'msg': msg, 'result': result})

    def queryResult(result=None):
        return jsonify({'code': ERROR_CODE, 'msg': "调用成功", 'result': queryToDict(result)})

    def page(page):
        items = queryToDict(page.items)
        result = {"page":page.page,"pages":page.pages,"per_page":page.per_page,"total":page.total,"items":items}
        return jsonify({'code': SUCCESS_CODE, 'msg': None, 'result': result})

def queryToDict(models):
    if (isinstance(models, list)):
        if(len(models)==0):
            return []
        if (isinstance(models[0], Model)):
            lst = []
            for model in models:
                gen = model_to_dict(model)
                dit = dict((g[0], g[1]) for g in gen)
                lst.append(dit)
            return lst
        else:
            res = result_to_dict(models)
            return res
    else:
        if (models is None):
            return {}
        elif (isinstance(models, Model)):
            gen = model_to_dict(models)
            dit = dict((g[0], g[1]) for g in gen)
            return dit
        else:
            res = dict(zip(models.keys(), models))
            find_datetime(res)
            return res

# 当结果为result对象列表时，result有key()方法
def result_to_dict(results):
    res = [dict(zip(r.keys(), r)) for r in results]
    # 这里r为一个字典，对象传递直接改变字典属性
    for r in res:
        find_datetime(r)
    return res

def model_to_dict(model):  # 这段来自于参考资源
    for col in model.__table__.columns:
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(model, col.name))
        elif isinstance(col.type, Numeric):
            value = float(getattr(model, col.name))
        else:
            value = getattr(model, col.name)
        yield (col.name, value)

def find_datetime(value):
    for v in value:
        if (isinstance(value[v], cdatetime)):
            value[v] = convert_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改

def convert_datetime(value):
    if value:
        if (isinstance(value, (cdatetime, DateTime))):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        elif (isinstance(value, (date, Date))):
            return value.strftime("%Y-%m-%d")
        elif (isinstance(value, (Time, time))):
            return value.strftime("%H:%M:%S")
    else:
        return ""

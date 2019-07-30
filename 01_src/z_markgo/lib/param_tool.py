# 将dict_parm（dict类型）参数设置到obj对象中
def set_dict_parm(obj,dict_parm):
    for parm in dict_parm:
        setattr(obj, parm, dict_parm[parm])  # 相当于obj.name = value赋值语句


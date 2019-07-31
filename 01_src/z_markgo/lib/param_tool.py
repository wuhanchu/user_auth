# 将dict_parm（dict类型）参数设置到obj对象中
def set_dict_parm(obj,dict_parm):
    for parm in dict_parm:
        setattr(obj, parm, dict_parm[parm])  # 相当于obj.name = value赋值语句

# 将object对象的dict对象
def model_to_dict(obj):
    dict_obj = obj.__dict__
    dict_obj.pop('_sa_instance_state', None)
    return dict_obj
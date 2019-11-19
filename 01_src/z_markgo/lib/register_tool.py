import psutil,base64,json,datetime,os
from lib import rsa_tool
#获取网卡名称和其ip地址，不包括回环
def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k, v in info.items():
        if v[0].address != '127.0.0.1':
            netcard_info.append(v[0].address)
            if len(netcard_info)>0:
                break
    return ",".join(netcard_info)

def get_machineInfo():
    res = get_netcard()
    res = rsa_tool.pub_encrypt(res.encode("utf-8"))
    print("res:",res)
    res = str(base64.b64encode(res),"utf-8")
    return res

def check_license(lic_info):
    try:
        lic_info = rsa_tool.pub_decrypt(lic_info)
        res = json.loads(lic_info)
        # 机器码不匹配
        if res["machineInfo"] != get_netcard():
            return False, "机器码不匹配"
        if res["dueTime"] !=None and datetime.datetime.strptime(res["dueTime"], '%Y-%m-%d').date() < datetime.datetime.now().date():
            return False,"证书已过期,有效期截止：%s"%res["dueTime"]
        res.pop("machineInfo")
        return True, res
    except:
        return False,"证书解析错误"

def create_license(machineInfo,dueTime,customName):
    machineInfo = base64.b64decode(machineInfo.encode("utf-8"))
    machineInfo = rsa_tool.pri_decrypt(machineInfo)
    print(machineInfo)
    lic = {
        "machineInfo": str(machineInfo,"utf-8"),
        "registTime": datetime.datetime.now().strftime('%Y-%m-%d'),
        "dueTime":dueTime,
        "customName": customName,
        "productName":"会议系统（z_meeting）",
    }
    lic = json.dumps(lic)
    print(lic)
    lic = rsa_tool.pri_encrypt(lic.encode("utf-8"))
    with open("./license_%s(%s).lic"%(dueTime,customName),"w") as f:
        f.write(str(base64.b64encode(lic),"utf-8"))

def check_licfile():
    # 判断证书是否存在，如果存在就返回有效时间
    if os.path.exists("./license"):
        with open("./license") as lic:
            lic_info = lic.read()
            lic_info = base64.b64decode(lic_info)
            is_enable, lic_info = check_license(lic_info)
            if is_enable:
                return True
            else:
                return False
    else:
        return False


if __name__ == '__main__':
    machineInfo = "eFWsX0J6dCpgxF+HN3iQCAGY9/HL+PSfoQ3YQA/BD9kFQRrjE5K2LjR/J7yw80M2YwTbQkXVKOWRIcLBFiOhnUKn3oBHr5c+f05rvl6Q49XtDF0MErloTL3LVnsNLEP3sHxHlQrCg44TvK91+rJs4TKzNV+bQSzdxXRD4c6Y7iuSmD/lWoHKyuDVceHvq+w278mCsbc88k++j9kF47nPwr8T4b6hILsTeNJg5or9h+fQ1zrHAdRRINTO4VZAPlHE6Qp5BuP/OvFErslelxpYWkcWwUrdYWZmw+7MkIek19BmeNXbXDh8J8RLNmb8xrVZxOLv8OiLZy/30a73SpRvtw=="
    # machineInfo = base64.b64decode(machineInfo.encode("utf-8"))
    # print(machineInfo)
    # machineInfo = rsa_tool.pri_decrypt(machineInfo)
    # print(str(machineInfo,"utf-8"))
    create_license(machineInfo,"2020-11-30","测试公司")

    # s = "你好"
    # print(s.encode("utf-8"))
    # print(str(s.encode("utf-8"),"utf-8"))
    # s_b64 =  str(base64.b64encode(s.encode("utf-8")),"utf-8")
    # print(s_b64)
    # print(str(base64.b64decode(s_b64.encode("utf-8")),"utf-8"))
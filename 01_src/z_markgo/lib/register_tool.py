import psutil,base64,json,datetime,os
from lib import rsa_tool
#获取网卡名称和其ip地址，不包括回环
def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for i in range(len(v)):
            #print("family:%s, addr:%s，netmask=%s ,ptp=%s"%(v[i].family,v[i].address,v[i].netmask,v[i].ptp))
            if str(v[i].family).endswith("AF_LINK") or str(v[i].family).endswith("AF_PACKET"):
                if(v[i].address != "00:00:00:00:00:00"):
                    netcard_info.append(v[i].address)
        if len(netcard_info)>0:
            break
        #print("--------------------------")
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
        "productName":"标注狗（z_markgo）",
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
    # machineInfo = "JzO09kRMIq6JCdLazQJ3gnJJGnxqs1fYzgn2vru41IguxsFkCV4NgAlCTguYjsG3h9MfW7yttWvTu9eGyxKm/1xUrbPE45yISfutrUx3K+xRfPfHiVR8NiGepD3uBDIOD6GQ97SsSb3oFFeYidLd5+x76+5OPlu8jnSFljJeltpdr0hGrqO0S74HfRuYB+EXwEJ6Tj9L4r8I4Wf5EUcEuMbeQGUcEJgQiIxjtKaePM26DTZK3pLPUtWMYmijMAaIoP1wPcIEfHaWvuFCi+wCJFYONxn+CONFhrwU49dNKWxj343T7NzZD3U8dLjDkaMoKQRNRCxwjKYiexhGImU9Wg=="
    # machineInfo = base64.b64decode(machineInfo.encode("utf-8"))
    # print(machineInfo)
    # machineInfo = rsa_tool.pri_decrypt(machineInfo)
    # print(str(machineInfo,"utf-8"))
    # create_license(machineInfo,"2020-01-30","江海测试")
    print (get_netcard())
    # s = "你好"
    # print(s.encode("utf-8"))
    # print(str(s.encode("utf-8"),"utf-8"))
    # s_b64 =  str(base64.b64encode(s.encode("utf-8")),"utf-8")
    # print(s_b64)
    # print(str(base64.b64decode(s_b64.encode("utf-8")),"utf-8"))


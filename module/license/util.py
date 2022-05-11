import base64
import datetime
import json
import os

import psutil

from frame.util import rsa_tool


def get_net_card():
    """
    获取网卡名称和其ip地址，不包括回环

    :return:
    """
    net_card_info = []
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for i in range(len(v)):
            # print("family:%s, addr:%s，netmask=%s ,ptp=%s"%(v[i].family,v[i].address,v[i].netmask,v[i].ptp))
            if str(v[i].family).endswith("AF_LINK") or str(v[i].family).endswith("AF_PACKET"):
                if (v[i].address != "00:00:00:00:00:00"):
                    net_card_info.append(v[i].address)
        if len(net_card_info) > 0:
            break
        # print("--------------------------")
    return ",".join(net_card_info)


def get_machine_info():
    """
    获取机器码
    :return:
    """
    res = get_net_card()
    res = rsa_tool.pub_encrypt(res.encode("utf-8"))
    print("res:", res)
    res = str(base64.b64encode(res), "utf-8")
    return res


def check_license(content):
    """
    检查证书信息
    :param content:
    :return:
    """
    try:
        lic_info = base64.b64decode(content)
        lic_info = rsa_tool.pub_decrypt(lic_info)
        record = json.loads(lic_info)

        # 机器码不匹配
        if record["machine_info"] != get_net_card():
            return False, record, "证书无效，机器码不匹配"
        
        if record["due_time"] and datetime.datetime.strptime(record["due_time"],
                                                             '%Y-%m-%d').date() < datetime.datetime.now().date():
            return False, "证书已过期,有效期截止：%s" % record["due_time"]
        return True, record, "证书解析成功"
    except:
        return False, None, "证书解析错误"


def create_license(machine_info, product_key, due_time, custom_name):
    """
    :param machine_info:
    :param product_key:
    :param due_time:
    :param custom_name:
    :return:
    """
    machine_info = base64.b64decode(machine_info.encode("utf-8"))
    machine_info = rsa_tool.pri_decrypt(machine_info)

    lic = {
        "machine_info": str(machine_info, "utf-8"),
        "registered_time": datetime.datetime.now().strftime('%Y-%m-%d'),
        "due_time": due_time,
        "custom_name": custom_name,
        "product_key": product_key,
    }
    lic = json.dumps(lic)
    lic = rsa_tool.pri_encrypt(lic.encode("utf-8"))
    return str(base64.b64encode(lic), "utf-8")


def check_license_file():
    """
     判断证书是否存在，如果存在就返回有效时间
    :return:
    """
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

#
# if __name__ == '__main__':
#     machine_info = "XxZxRTArmStX/dE/4ReRqFCSeOkdCYXPVpmgLSRXH+qjI5Hz6IUtZ9gvhYKYMKH5dTh1wP0XqczwMZV4Tmg918ihPqqUam9OQUfJq6J409kLqjERX2EBN9ahpR/7UFLcgSrDcapkvs6ANtAmmRlQu6dVK4VFzLfzJmn35KKZ/ATPGTKtOD0JjiCiNrOSs2aswxNwkSiNzZ1CgJjR71nq9xstp+v+5TV+AfWD6M2A3xEDFsAQ+Zq5Afd0qhGVxiBMJp/KxHn9DhKLRkuZhQQsJSjwzOmXkmruq3T0Bbbvs1dZE6SNePT8ZSVHvIk6z+gTjXjrYFqiuvfR3N8ZCPNtFw=="
#     # machine_info = base64.b64decode(machine_info.encode("utf-8"))
#     # print(machine_info)
#     # machine_info = rsa_tool.pri_decrypt(machine_info)
#     # print(str(machine_info,"utf-8"))
#     create_license(machine_info, "2020-12-30", "掌数知料")
#     # print (get_net_card())
#     # s = "你好"
#     # print(s.encode("utf-8"))
#     # print(str(s.encode("utf-8"),"utf-8"))
#     # s_b64 =  str(base64.b64encode(s.encode("utf-8")),"utf-8")
#     # print(s_b64)
#     # print(str(base64.b64decode(s_b64.encode("utf-8")),"utf-8"))

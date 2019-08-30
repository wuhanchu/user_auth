#asr 工具集
import requests,config
import json,os
from lib import com_tool
from requests_toolbelt import MultipartEncoder
import pandas as pd

userid="13811002233"
token= "12345678"

def client_post_mutipart_formdata_requests(request_url, datas ):
    m = MultipartEncoder(datas)
    # 发送请求报文到服务端
    r = requests.post(request_url,  headers={'Content-Type': m.content_type}, data=m )
    # 获取服务端的响应报文数据
    responsedata = r.text
    # 返回请求响应报文
    return responsedata

# 天聪asr
def tc_asr(asr_url,filepath,framerate=16000) :
    (fileDir, filename) = os.path.split(filepath)
    my_user = userid
    if framerate == 8000:
        my_user = userid + "-8K"
    with open(filepath, 'rb') as f:
        data = {
            "userid": my_user,
            "token": token,
            "sid": "test123456",
            'file': (filename, f, 'application/wav')
        }
        res = client_post_mutipart_formdata_requests(com_tool.url_join(asr_url,"dotcasr"), data)
    res = json.loads(res)
    return res

#讯飞asr
def xf_asr(asr_url,filepath):

    return None

if __name__ == '__main__':
    # asr_url = "http://39.105.193.154:15098/"
    asr_url = "http://192.168.1.150:34568/"
    # asr_url = "http://dataknown.tpddns.cn:3998"
    # filepath = r"C:\Users\czc\Desktop\txt\item\488_003.wav"
    filepath = r"C:\Users\czc\Desktop\txt\wav-8k\201805180003187692024.wav"
    res = tc_asr(asr_url, filepath,8000)
    print(res)


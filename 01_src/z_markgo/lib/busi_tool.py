## 这个文件主要保存业务相关函数
import os
from lib import asr_tool
import logging

logger = logging.getLogger('flask.app')

#判断是使用机转文档还是默认文本
def is_asr(AiService):
    if AiService.name == "话术文本" :
        return False
    else:
        return True
def get_item_root_path():
    work_dir = os.getcwd()
    return os.path.join(os.path.dirname(work_dir), "z_markgo_items")

def tc_asr(item_id,asr_url,filepath):
    try:
        res = asr_tool.tc_asr(asr_url,filepath)
        if (res['errCode'] == '0'):
            return item_id, res['result']
    except Exception as e:
        logger.error("asr解析失败！（item:%s）" % item_id)
    return item_id,None

def test_par(a,*args):
    print(a)
    print(args)

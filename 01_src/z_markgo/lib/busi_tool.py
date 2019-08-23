## 这个文件主要保存业务相关函数
import os,logging,json,shutil
from lib import asr_tool,wav_tool,com_tool

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
        tmp_path = os.path.join(os.path.dirname(filepath),str(item_id)+"_tmp")
        com_tool.create_if_dir_no_exists(tmp_path)
        # 子音频文件信息
        sub_items,framerate = wav_tool.vad_cut(filepath,tmp_path)
        for sub_item in sub_items:
            res = asr_tool.tc_asr(asr_url,sub_item["path"],framerate)
            if (res['errCode'] == '0'):
                sub_item["txt"] = res['result']
                sub_item.pop("path")
            else:
                raise RuntimeError("asr解析失败！（item:%s）" % item_id)
        json_items = json.dumps(sub_items,ensure_ascii=False)
        logger.info("asr解析成功！（items:%s）" % json_items)
        return item_id,json_items
    except Exception as e:
        logger.error("asr解析失败！%s" % e)
    finally:
        shutil.rmtree(tmp_path)
    return item_id,None

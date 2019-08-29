## 这个文件主要保存业务相关函数
import os,logging,json,shutil
from lib import asr_tool,wav_tool,com_tool,asr_score_tool

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
        tmp_path = os.path.join(get_item_root_path()+"_tmp",str(item_id))
        com_tool.create_if_dir_no_exists(tmp_path)
        # 子音频文件信息
        sub_items,framerate = wav_tool.vad_cut(filepath,tmp_path)
        for sub_item in sub_items:
            res = asr_tool.tc_asr(asr_url,sub_item["path"],framerate)
            if (res['errCode'] == '0'):
                sub_item["txt"] = res['result']
                sub_item.pop("path")
            # todo 处理报错问题
            elif res['errCode'] == '-2':
                sub_item["txt"] = res['result']
                logger.warn("asr解析失败，%s！（path:%s）" %(str(res),sub_item["path"]))
                sub_item.pop("path")
            else:
                raise RuntimeError("asr解析失败，%s！（path:%s）" %(str(res),sub_item["path"]))
        json_items = json.dumps(sub_items,ensure_ascii=False)
        return item_id,json_items
    except Exception as e:
        logger.error("asr解析失败！%s" % e)
    finally:
        shutil.rmtree(tmp_path)
    return item_id,None

def mark_score(mark_txt,inspection_txt):
    mark_list = json.loads(mark_txt)
    mark_txt = ""
    for item in mark_list:
        mark_txt = mark_txt + item["txt"]
    inspection_list = json.loads(inspection_txt)
    inspection_txt = ""
    for item in inspection_list:
        inspection_txt = inspection_txt + item["txt"]
    print(inspection_txt)
    print(mark_txt)

    op2, m, s1, op, s2, I_COUNT_PCT, D_COUNT_PCT, S_COUNT_PCT = asr_score_tool.med_classic_gui(mark_txt,inspection_txt)
    accuracy = 1 - (m / len(s1.replace(" ", '')))
    return accuracy

if __name__ == '__main__':
    mark_txt = r"""[{"i":1,"st":3000,"et":6000,"txt":"test1"},{"i":2,"st":7000,"et":9000,"txt":"test1"},{"i":3,"st":10000,"et":13000,"txt":"test1"},{"i":4,"st":10000,"et":13000,"txt":"test1"},{"i":5,"st":10000,"et":13000,"txt":"test1"}]"""
    inspection_txt = r"""[{"i":1,"st":3000,"et":6000,"txt":"test一"},{"i":2,"st":7000,"et":9000,"txt":"test一"},{"i":3,"st":10000,"et":13000,"txt":"test一"},{"i":4,"st":10000,"et":13000,"txt":"test一"},{"i":5,"st":10000,"et":13000,"txt":"test一"}]"""
    print (mark_score(mark_txt,inspection_txt))
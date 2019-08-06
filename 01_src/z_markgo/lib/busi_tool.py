## 这个文件主要保存业务相关函数
import os
#判断是使用机转文档还是默认文本
def is_asr(AiService):
    if AiService.name == "话术文本" :
        return False
    else:
        return True
def get_item_root_path():
    work_dir = os.getcwd()
    return os.path.join(os.path.dirname(work_dir), "z_markgo_items")

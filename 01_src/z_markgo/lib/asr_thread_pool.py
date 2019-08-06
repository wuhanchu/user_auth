from concurrent.futures import ThreadPoolExecutor
from lib import asr_tool,busi_tool
from lib.models import *
import os,logging

logger = logging.getLogger('flask.app')

# python 线程池
class asr_thread_pool(object):
    '工作线程池'
    item_root_path = busi_tool.get_item_root_path();
    taskids =  {}
    executor = ThreadPoolExecutor(max_workers=8)
    def submit(self,project_id,func,item,asr_url):
        # 任务池加载任务
        if project_id not in self.taskids:
            self.taskids[project_id] = [item.id]
        else:
            self.taskids[project_id].append(item.id)
        print("加载任务（%s） project:%s ,itme:%s" % (len(self.taskids[project_id]),project_id, item.id))
        self.executor.submit(func,item,asr_url).add_done_callback(self.call_back)

    def call_back(self,res):
        self.taskids[res._result[0]].remove(res._result[1]);
        print(self.taskids)
    # 判断项目是否在队列中存在
    def check(self,project_id,func,args):
        if project_id not in self.taskids:
            return len(self.taskids[project_id])
        else:
            return 0

    def batch_add_items(self,project,items):
        ai_service = AiService.query.get(project.ai_service)
        for item in items:
            self.submit(project.id,self.asr_item,item,ai_service.service_url)

    def asr_item(self,item,asr_url):
        filepath = os.path.join(self.item_root_path, item.filepath)
        try:
            res = asr_tool.tc_asr(asr_url,filepath)
        except Exception as e:
            res = {"errCode":"-1","result":e}

        if(res['errCode']=='0'):
            item.asr_txt = res['result']
            # todo 更新到数据库

            print("insert to db")
            return item.project_id,item.id
        else:
            logger.error("asr解析失败！（project:%s ,item:%s）"%(item.project_id,item.id))
            return False,item.project_id,item.id

#单例模式
asr_thread_pool = asr_thread_pool()

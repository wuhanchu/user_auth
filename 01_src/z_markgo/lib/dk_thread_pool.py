# python 线程池
from concurrent.futures import ThreadPoolExecutor

class dk_thread_pool(object):
    '工作线程池'
    executor = ThreadPoolExecutor(max_workers=8)
    def submit(self,func,args):
        # 任务池加载任务
        self.executor.submit(func,args)
#单例模式
dk_thread_pool = dk_thread_pool()

# 常用函数，时间格式，文件读写等。
import datetime

#获取当前日期，格式%Y-%m-%d %H:%M:%S
def get_curr_date():
    curr_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 日期格式化
    return curr_date

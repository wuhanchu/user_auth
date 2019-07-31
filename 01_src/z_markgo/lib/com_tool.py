# 常用函数，时间格式，文件读写等。
import datetime,zipfile,os

#获取当前日期，格式%Y-%m-%d %H:%M:%S
def get_curr_date():
    curr_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 日期格式化
    return curr_date
#解压单个文件到目标文件夹
def unzip_file(src_file, dest_dir, password):
    if password:
        password = password.encode()
    zf = zipfile.ZipFile(src_file)
    try:
        zf.extractall(path=dest_dir, pwd=password)
    except RuntimeError as e:
        print(e)
    zf.close()

#遍历目录（子目录），返回所有文件路径
def EnumPathFiles(path, callback):
    if not os.path.isdir(path):
        print('Error:"',path,'" is not a directory or does not exist.')
        return
    list_dirs = os.walk(path)

    for root, dirs, files in list_dirs:
        for d in dirs:
            EnumPathFiles(os.path.join(root, d), callback)
        for f in files:
            callback(root, f)

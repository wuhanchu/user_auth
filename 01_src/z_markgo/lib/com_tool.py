# 常用函数，时间格式，文件读写等。
import datetime,zipfile,os,hashlib,base64

#获取当前日期，格式%Y-%m-%d %H:%M:%S
def get_curr_date():
    curr_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 日期格式化
    return curr_date
#解压单个文件到目标文件夹
def unzip_file(src_file, dest_dir, password=None):
    if password:
        password = password.encode()
    zf = zipfile.ZipFile(src_file)
    try:
        zf.extractall(path=dest_dir, pwd=password)
    finally:
        zf.close()

#遍历目录（子目录），返回所有文件路径
def enum_path_files(path):
    file_paths = []
    if not os.path.isdir(path):
        print('Error:"',path,'" is not a directory or does not exist.')
        return
    list_dirs = os.walk(path)
    for root, dirs, files in list_dirs:
        for f in files:
            file_paths.append(os.path.join(root,f))
    return file_paths
# url 路径拼接
def url_join(par_url,sub_url):
    if par_url.endswith("/"):
        if sub_url.startswith(("/")):
            sub_url = sub_url[1:]
    else:
        if not sub_url.startswith(("/")):
            sub_url = "/" + sub_url
    return par_url + sub_url
# 获取md5代码
def get_MD5_code(str):
    hash_md5 = hashlib.md5()
    # 计算
    str = str.encode('utf-8', errors='ignore')
    hash_md5.update(str)
    # 获取计算结果(16进制字符串，32位字符)
    md5_str = hash_md5.hexdigest()
    # 打印结果
    # print(md5_str)
    return md5_str

def get_base64():
    res = base64.b64encode(str)
    return res
def from_base64(str):
    res = base64.b64decode(str)
    return res

if __name__ == '__main__':
    # file_paths = enum_path_files(r'E:\workspace_python\z_markgo\01_src\z_markgo_items\2')
    # for i in file_paths:
    #     print(i)
    # unzip_file("C:\\Users\\czc\\Desktop\\txt\\item\\item.zip","C:\\Users\\czc\\Desktop\\txt\\item\\bak")
    # get_MD5_code("hello world")

    print(from_base64("eUFsOVBPOXNBNE5LWWhjclhmQU9YeGxEOkRhcm1yQ2tlQTA0clY4dDh2QTRtVFhoTXZuN25FVXdlRTA3Smd2V2hFVnBHc3VrSw=="))

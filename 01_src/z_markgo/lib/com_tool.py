#!/usr/bin/python
# -*- coding: UTF-8 -*-

import base64
import datetime
import hashlib
import os
import time
import zipfile
# 常用函数，时间格式，文件读写等。
from pathlib import Path


# 获取当前日期，格式%Y-%m-%d %H:%M:%S
def get_curr_date():
    curr_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 日期格式化
    return curr_date


# 解压单个文件到目标文件夹
def unzip_file(src_file, dest_dir, password=None):
    if password:
        password = password.encode()
    zf = zipfile.ZipFile(src_file)

    try:
        for fn in zf.namelist():
            extracted_path = Path(zf.extract(fn, dest_dir))
            if extracted_path.exists() and not (fn.startswith(".") or r"/." in fn or r"\." in fn):
                try:
                    extracted_path.rename(dest_dir+"/"+fn.encode('cp437').decode('utf-8'))
                except:
                    extracted_path.rename(dest_dir+"/"+fn.encode('cp437').decode('gbk','ignore'))
    finally:
        zf.close()

def zip_dir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


# 判断文件目录是否存在，不存在则创建
def create_if_dir_no_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


# 遍历目录（子目录），返回所有文件路径
def enum_path_files(path):
    file_paths = []
    if not os.path.isdir(path):
        print('Error:"', path, '" is not a directory or does not exist.')
        return
    list_dirs = os.walk(path)
    for root, dirs, files in list_dirs:
        for f in files:
            file_paths.append(os.path.join(root, f))
    return file_paths


# url 路径拼接
def url_join(par_url, sub_url):
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


def random_value():
    t = time.time()
    value = str(int(t * 1000))
    # int(random.uniform(10000, 100000))
    return value


def if_null(arg1, arg2):
    if arg1:
        return arg1
    else:
        return arg2


if __name__ == '__main__':
    # file_paths = enum_path_files(r'E:\workspace_python\z_markgo\01_src\z_markgo_items\2')
    # for i in file_paths:
    #     print(i)
    # unzip_file("C:\\Users\\czc\\Desktop\\txt\\item\\item.zip","C:\\Users\\czc\\Desktop\\txt\\item\\bak")
    # get_MD5_code("hello world")
    t = time.time()

    print(int(t))  # 毫秒级时间戳

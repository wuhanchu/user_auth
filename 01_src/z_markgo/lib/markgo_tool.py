# -*- coding:utf-8 -*-
import numpy as np,chardet
import re, sys, os
from lib import txt_compare



def splite_file(filepath):
    dir_path = filepath[0:filepath.rindex('.')]
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    else:
        print("目录已存在：%s" % dir_path)
    print("切分文件保存路径：%s"%dir_path)
    with open(filepath,encoding='utf-8') as src_file:
        lines = src_file.readlines()
        for i in range(len(lines)):
            line = lines[i]
            sub_filename = line[0:line.index(" ")]
            line = line[len(sub_filename):].replace(" ", "").replace("\n", "")
            sub_filename = sub_filename[sub_filename.rindex('/')+1:sub_filename.rindex('.')]+".txt"
            with open(os.path.join(dir_path,sub_filename),"w",encoding="utf-8") as sub_file:
                sub_file.write(line)
                print("写入文件：%s"%sub_filename)

# 多种asr服务的文本比对，并将结果写入到excel
def txt_compares(args):
    mark_path = args[0]
    res_arr = []
    dir_names = []
    for i in range(1,len(args)):
        print("文本比较：%s %s"%(mark_path,args[i]))
        res = txt_compare.batch_file_classice(mark_path,args[i])
        dir_names.append(os.path.basename(args[i]))
        res_arr.append(res)
    with open (os.path.join(os.path.dirname(mark_path),"res.csv"),"w",encoding="gbk") as res_csv :
        res_csv.write("文件名,文件夹名,字准,插入率,删除率,替换率\n")
        for j in range(-1,len(res_arr[0])-1):
            print(j)
            for i in range(len(res_arr)):
                # {"accuracy": accuracy,"I_COUNT_PCT": I_COUNT_PCT, "D_COUNT_PCT": D_COUNT_PCT, "S_COUNT_PCT": S_COUNT_PCT}
                if i == 0:
                    file_name = res_arr[i][j]["filename"]
                else:
                    file_name = ""
                print(("%s,%s,%s,%s,%s,%s\n" % (
                file_name, dir_names[i], res_arr[i][j]["accuracy"], res_arr[i][j]["I_COUNT_PCT"]
                , res_arr[i][j]["D_COUNT_PCT"], res_arr[i][j]["S_COUNT_PCT"])))
                res_csv.write("%s,%s,%s,%s,%s,%s\n" % (
                file_name, dir_names[i], res_arr[i][j]["accuracy"], res_arr[i][j]["I_COUNT_PCT"]
                , res_arr[i][j]["D_COUNT_PCT"], res_arr[i][j]["S_COUNT_PCT"]))

def txt_decode(dir_path):
    file_paths = txt_compare.enum_path_files(dir_path)
    for file_path in file_paths:
        txt_compare.standardized_file_encode(os.path.join(dir_path,file_path))

if __name__ == '__main__':
    sys.argv = [r"markgo_tool.pyc",r"txt_compare",r"F:\Z-ASR\33\mark",r"F:\Z-ASR\33\ths脱敏录音撰写",r"F:\Z-ASR\33\脱敏录音_8k_dfzq_txt",r"F:\Z-ASR\33\脱敏录音_8k_通用_txt"]
    # sys.argv = [r"markgo_tool.pyc",r"splite_file",r"F:\Z-ASR\中信建投测试数据\数据整理\tc.txt"]
    # sys.argv = [r"markgo_tool.pyc", r"txt_decode", r"F:\Z-ASR\同花顺\脱敏录音撰写"]
    # txt_compare.standardized_file_encode(r"F:\Z-ASR\同花顺\12759_143720 - 副本.txt")
    # txt_compare.standardized_file_encode(r"F:\Z-ASR\同花顺\test.txt")
    print(r"""
===========================================
用法举例：
文件切分：python markgo_tool.pyc splite_file C:\Users\czc\Desktop\txt\txt_comp\mark_out.txt
文件编码转写：python markgo_tool.pyc txt_decode F:\Z-ASR\同花顺\脱敏录音撰写
多类型txt_compare ：python markgo_tool.pyc txt_compare F:\Z-ASR\中信建投测试数据\数据整理\mark F:\Z-ASR\中信建投测试数据\数据整理\tc F:\Z-ASR\中信建投测试数据\数据整理\ths F:\Z-ASR\中信建投测试数据\数据整理\zs
===========================================     

    """)

    # 读取文件
    if sys.argv[1] == "splite_file" :
        splite_file(sys.argv[2])
    elif sys.argv[1] == "txt_decode" :
        txt_decode(sys.argv[2])

    else:
        txt_compares(sys.argv[2:])
    # path = r"F:\Z-ASR\中信建投测试数据\数据整理\tc.txt"
    # splite_file(path)
    # txt_compares(r"F:\Z-ASR\中信建投测试数据\数据整理\mark1",r"F:\Z-ASR\中信建投测试数据\数据整理\tc",r"F:\Z-ASR\中信建投测试数据\数据整理\ths",r"F:\Z-ASR\中信建投测试数据\数据整理\zs")

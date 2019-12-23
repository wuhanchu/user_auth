# ffmpeg 音频转换工具，支持linux和windows下运行，依赖ffmpeg程序包
# -*- coding:utf-8 -*-
import os, tempfile

ffmpeg_tmp = os.path.join(tempfile._get_default_tempdir(), "ffmpeg_tmp.log")

# -ar 8000 -ac 1 8k，单声道
# -ar 16000 -ac 1  16k，单声道
# E:\workspace_python\z_markgo\01_src\z_markgo\lib\ffmpeg.exe
#   -i  C:\Users\czc\Desktop\asr\开户审核退回\1506116.V3
#   -f wav -ar 16000 C:\Users\czc\Desktop\asr\开户审核退回\1506116.wav
# -y 覆盖
# 参数说明
def ffmpeg(input_path,output_path,f="wav", ar=16000 ,ac=1):
    cmd = """ffmpeg -y -i "%s" -f %s -ar %s -ac %s "%s" > %s 2>&1 """  % (input_path, f, ar,ac, output_path,ffmpeg_tmp)
    print('执行ffmpeg命令：%s'%cmd)
    res = (os.system(cmd) == 0)
    if res == False :
        #执行出错了
        with open(ffmpeg_tmp) as log:
            raise RuntimeError(log.read())
    else:
        return res



# 主程序运行
if __name__ == '__main__':
    input = r"C:\Users\czc\Desktop\asr\开户审核退回\1506116.V3"
    output = input + ".wav"
    ffmpeg(input,output)

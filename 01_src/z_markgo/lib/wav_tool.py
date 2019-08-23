#coding=utf-8

import wave
import numpy as np
import os

MAX_EN = 1000

def get_wav_info(wav_path):
    with wave.open(wav_path, "rb") as f:
        print(f.getparams())
        return f.getparams()

def check_wav_format(wav_path):
    params = get_wav_info(wav_path)
    # 判断音频是否是单声道
    if params.nchannels != 1 :
        return -1
    else:
        # 返回音频频率 16000 或 8000 是支持的，其他频率无法支持
        return params.framerate

# 音频切割
def cut_wav(wave_data, begin,end,nchannels,sampwidth, framerate,save_path):
    # print("cut_wav: %s----%s len:%s" % (begin,end,(end-begin)/16000))
    file_name = os.path.join(save_path,"%s_%s.wav"%(begin,end))
    temp_dataTemp = wave_data[begin:end]
    temp_dataTemp.shape = 1, -1
    temp_dataTemp = temp_dataTemp.astype(np.short)  # 打开WAV文档
    with wave.open(r"" + file_name, "wb") as f:
        # 配置声道数、量化位数和取样频率
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        # 将wav_data转换为二进制数据写入文件
        f.writeframes(temp_dataTemp.tostring())

    return file_name


def check_avg(arr,begin,end):
    avg_en = 0
    for i in range(begin,end):
        avg_en = avg_en + abs(arr[i])
    avg_en = avg_en/(end-begin)
    return avg_en

# 根据音量进行断句
def vad_cut(wave_path,save_path):
    global MAX_EN
    with wave.open(wave_path) as file:
        nchannels, sampwidth, framerate, nframes = file.getparams()[:4]

        sample_time = 1 / framerate  # 采样点的时间间隔
        time = nframes / framerate  # 声音信号的长度
        SAMPLE_STEP = int(framerate / 10)

        str_data = file.readframes(nframes)
        wave_data = np.fromstring(str_data, dtype=np.int16)
    # 上一个切割的音频
    items = []
    last_wav = 0
    begin = 0
    ind = 0
    # 静音检测次数
    MAX_EN = check_avg(wave_data, 0, SAMPLE_STEP * 3)
    print("静音音量：%s"%MAX_EN)
    while begin < wave_data.shape[0] - SAMPLE_STEP * 4:
        step = SAMPLE_STEP
        if ind == 0:
            step = SAMPLE_STEP * 4
        if check_avg(wave_data, begin, begin + step) < MAX_EN:
            ind = ind + 1
        else:
            if last_wav == 0 :
                last_wav = 1
                ind = 0
            if ind > 0 and (begin-last_wav)/SAMPLE_STEP>5 :
                print("时长%s:%s" % ((begin - last_wav) / SAMPLE_STEP, (begin - last_wav) / SAMPLE_STEP > 5))  # 表示音频段大于5ms
                path = cut_wav(wave_data, last_wav, begin, nchannels, sampwidth, framerate,save_path)
                item = {"i": len(items) + 1, "st": int(last_wav*1000/framerate), "et": int(begin*1000/framerate), "path": path}
                items.append(item)
                last_wav = begin
                ind = 0
        begin = begin + step;
    path = cut_wav(wave_data, last_wav, len(wave_data) - 1, nchannels, sampwidth, framerate,save_path)
    item = {"i": len(items) + 1, "st": int(last_wav*1000/framerate), "et": int(begin*1000/framerate), "path": path}
    items.append(item)
    return items,framerate

if __name__ == '__main__':
    # wave_path = r"D:\gs.wav"
    # wave_path = r"C:\Users\czc\Desktop\txt\item\488_001.wav"
    wave_path = r"C:\Users\czc\Desktop\txt\wav-8k\201805180004181023655.wav"
    vad_cut(wave_path,r"D:\tmp")






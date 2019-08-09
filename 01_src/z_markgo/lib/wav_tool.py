#coding=utf-8

import wave
import numpy as np
import matplotlib as plt
import os

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


if __name__ == '__main__':
    wave_path = r"D:\gs.wav"
    SAMPLE_STEP = 3
    MAX_EN = 100

    file = wave.open(wave_path)
    a = file.getparams().nframes  # 帧总数
    f = file.getparams().framerate  # 采样频率
    sample_time = 1 / f  # 采样点的时间间隔
    time = a / f  # 声音信号的长度

    str_data = file.readframes(a)
    wave_data = np.fromstring(str_data, dtype=np.int16)
    # for i in range(wave_data.shape[0]-SAMPLE_STEP):
    #     avg_en = 0
    #     for j in range(SAMPLE_STEP):
    #         avg_en = avg_en + abs(wave_data[i + j])
    #     avg_en = avg_en/SAMPLE_STEP
    #     if avg_en < MAX_EN:
    #         print(avg_en)

    # print(audio_sequence)  # 声音信号每一帧的“大小”
    x_seq = np.arange(0, time, sample_time)



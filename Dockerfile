FROM  server.aiknown.cn:31003/z_ai_frame/alpine-python3:latest
COPY "./" "./"

RUN pip3 install  -i https://mirrors.aliyun.com/pypi/simple/  -r ./requirements.txt
RUN ln -sf /usr/bin/python3 /usr/bin/python

RUN chmod +x ./script/run.sh

CMD ./script/run.sh

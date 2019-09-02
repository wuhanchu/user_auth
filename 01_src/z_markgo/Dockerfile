FROM frolvlad/alpine-python3

ENV API_SERVER_HOME=/opt/www
WORKDIR "$API_SERVER_HOME"
COPY "./requirements.txt" "./"
COPY "./app/requirements.txt" "./app/"
COPY "./config.py" "./"
COPY "./tasks" "./tasks"
EXPOSE 5000

ARG INCLUDE_POSTGRESQL=false
ARG INCLUDE_UWSGI=false
RUN echo 'https://mirrors.aliyun.com/alpine/v3.9/main/' >/etc/apk/repositories && echo 'https://mirrors.aliyun.com/alpine/v3.9/community/' >>/etc/apk/repositories &&
    apk add --no-cache --virtual=.build_dependencies musl-dev gcc python3-dev libffi-dev linux-headers openssl-dev libxslt libxslt-dev &&
    apk --no-cache add tzdata &&
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&
    echo "Asia/Shanghai" >/etc/timezone &&
    cd /opt/www &&
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r tasks/requirements.txt &&
    invoke app.dependencies.install &&
    apk del .build_dependencies

COPY "./" "./"

RUN chown -R nobody "." &&
    if [ ! -e "./local_config.py" ]; then
        cp "./local_config.py.template" "./local_config.py"
    fi

USER nobody
CMD [ "invoke", "app.run", "--no-install-dependencies", "--host", "0.0.0.0" ]

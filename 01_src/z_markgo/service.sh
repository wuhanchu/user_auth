#!/usr/bin/env bash

APP_NAME=z_markgo.py

MYSQL_PWD=$2

usage() {
    echo "Usage: sh service.sh [start|stop|restart|status]"
    exit 1
}

is_exist(){
    pid=`ps -ef|grep $APP_NAME|grep -v grep|awk '{print $2}' `
    if [ -z "${pid}" ]; then
        return 1
    else
        return 0
    fi
}

start(){
    is_exist
    if [ $? -eq "0" ]; then
        echo "${APP_NAME} is already running. pid=${pid} ."
    else
		export AUTHLIB_INSECURE_TRANSPORT=True
		source activate py3.6
        nohup python $APP_NAME > ./markgo.nohup 2>&1 &
    fi
}

stop(){
    is_exist
    if [ $? -eq "0" ]; then
        kill -9 $pid
    else
        echo "${APP_NAME} is not running"
    fi
}

status(){
    is_exist
    if [ $? -eq "0" ]; then
        echo "${APP_NAME} is running. Pid is ${pid}"
    else
        echo "${APP_NAME} is NOT running."
    fi
}

restart(){
    stop
    start
}

case "$1" in
    "start")
    start
;;
    "stop")
    stop
;;
    "status")
    status
;;
    "restart")
    restart
;;
    *)
    usage
;;
esac
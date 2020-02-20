set -e
mixture=1
usage() {
    echo "Usage: sh service.sh [PYTHON_PATH&mixture&APP_NAME]"
    echo "运行service.sh脚本需要python路径（Python,Python3）、是否混淆代码标识（混淆1,不混淆0）和项目名"
    exit 1
}
if [ $# -eq 0 ];
then
    usage
fi
case "$1" in
    "start")
    usage
;;
esac
case "$2" in
    "start")
    usage
;;
    "1")
    #是否混淆 混淆1,不混淆0
    mixture=1
;;
    "0")
    #是否混淆 混淆1,不混淆0
    mixture=0
;;
    *)
    usage
;;
esac
case "$3" in
    "start")
    usage
;;
esac
if [[ -z "$1" || -z "$2" || -z "$3" ]]; then
    usage
fi
#进入脚本所在目录
currect_path=`cd $(dirname $0);pwd`
cd $currect_path
#设置python路径
PYTHON_PATH=$1
#设置项目名称
APP_NAME=$3
echo "项目名称${APP_NAME}"
echo "更新git代码"
git pull
#自动编译
echo "自动编译"
sh compileall.sh ${PYTHON_PATH} ${mixture} ${APP_NAME}
echo "删除运行中的容器"
docker stop $APP_NAME || echo "未发现旧容器"
docker rm $APP_NAME || echo "未发现旧容器"
echo "启动新容器"
docker run -d -p 5004:5004 --name $APP_NAME -e SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@192.168.1.150:3306/$APP_NAME?charset=utf8'  $APP_NAME:1.0.1

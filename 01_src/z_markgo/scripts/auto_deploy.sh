set -e
#进入脚本所在目录
currect_path=`cd $(dirname $0);pwd`
cd $currect_path
#设置项目名称
APP_NAME=z_markgo
VERSION=1.0.0.0
echo "项目名称${APP_NAME}"
echo "更新git代码"
git pull
#自动编译
echo "自动编译"
sh compileall.sh ${APP_NAME}
echo "删除运行中的容器"
docker stop $APP_NAME || echo "未发现旧容器"
docker rm $APP_NAME || echo "未发现旧容器"
echo "启动新容器"
docker run -d -p 5002:5002 --name $APP_NAME -e SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@192.168.1.150:3306/$APP_NAME?charset=utf8' $APP_NAME:${VERSION}


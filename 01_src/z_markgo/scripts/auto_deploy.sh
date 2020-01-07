set -e
git pull
#自动编译
echo "自动编译"
./script/compileall.sh
echo "删除运行中的容器"
docker stop z_markgo
docker rm z_markgo
echo "启动新容器"
docker run -d -p 5002:5002 --name z_markgo -e SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@192.168.1.150:3306/z_markgo?charset=utf8' -v ~/tmp/z_markgo_items:/opt/z_markgo_items z_markgo:1.0.0.0

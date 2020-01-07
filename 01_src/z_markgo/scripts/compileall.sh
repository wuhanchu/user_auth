#!/bin/bash
#设置项目名
APP_NAME=$1
VERSION=$2
set -e
#复制代码到
echo "复制代码到../${APP_NAME}_cp"
rm -rf ../../${APP_NAME}_cp
cp -r ../../${APP_NAME} ../../${APP_NAME}_cp
cd ../../${APP_NAME}_cp
echo "复制代码成功！"
echo "开始代码混淆！"
python36 ./scripts/obscure.py
echo "代码混淆结束！"

echo "开始代码编译！"
#选择python编译器版本
python3 -m compileall .
for file in $(find . -name '*.pyc');
do
    mv $file $(echo $file | sed 's/\.cpython-36//g'| sed 's/__pycache__\///g');
done
find -name "__pycache__" | awk '{print "rm -rf "$1}'|sh
find -name "*.py" | awk '{print "rm -rf "$1}'|sh
echo "代码编译完成！"
echo "开始生成docker 镜像！"
docker build . -t ${APP_NAME}:${VERSION}
echo "生成docker 镜像：${APP_NAME}:${VERSION}！"
rm -rf ../${APP_NAME}_cp
echo "删除临时文件${APP_NAME}_cp！"


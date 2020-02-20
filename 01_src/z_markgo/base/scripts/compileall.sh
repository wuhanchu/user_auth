#!/bin/bash
#设置python路径
PYTHON_PATH=$1
#是否混淆 混淆1,不混淆0
mixture=$2
#设置项目名
APP_NAME=$3
set -e
#复制代码到
echo "复制代码到../${APP_NAME}_cp"
rm -rf ../../${APP_NAME}_cp
cp -r ../../${APP_NAME} ../../${APP_NAME}_cp
cd ../../${APP_NAME}_cp
echo "复制代码成功！"
if test ${mixture} == 1; then
    echo "开始代码混淆！"
    ${PYTHON_PATH} ./scripts/obscure.py
    echo "代码混淆结束！"
elif [ ${mixture} == 0 ]; then
    echo '已选择不执行代码混淆！'
fi
echo "开始代码编译！"
#选择python编译器版本
${PYTHON_PATH} -m compileall .
for file in $(find . -name '*.pyc'); 
do
    mv $file $(echo $file | sed 's/\.cpython-36//g'| sed 's/__pycache__\///g');	
done
find -name "__pycache__" | awk '{print "rm -rf "$1}'|sh
find -name "*.py" | awk '{print "rm -rf "$1}'|sh
echo "代码编译完成！"
echo "开始生成docker 镜像！"
docker build . -t ${APP_NAME}:1.0.1
echo "生成docker 镜像：${APP_NAME}:1.0.1！"
rm -rf ../${APP_NAME}_cp
echo "删除临时文件${APP_NAME}_cp！"

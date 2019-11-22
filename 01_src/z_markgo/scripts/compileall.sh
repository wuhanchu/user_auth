#!/bin/bash
set -e
#复制代码到
echo "复制代码到../z_markgo_cp"
rm -rf ../z_markgo_cp
cp -r ../z_markgo ../z_markgo_cp
cd ../z_markgo_cp
echo "复制代码成功！"
echo "开始代码混淆！"
python ./scripts/obscure.py
echo "代码混淆结束！"

echo "开始代码编译！"
#选择python编译器版本
python -m compileall .
for file in $(find . -name '*.pyc'); 
do
    mv $file $(echo $file | sed 's/\.cpython-36//g'| sed 's/__pycache__\///g');	
done
find -name "__pycache__" | awk '{print "rm -rf "$1}'|sh
find -name "*.py" | awk '{print "rm -rf "$1}'|sh
echo "代码编译完成！"
echo "开始生成docker 镜像！"
docker build . -t z_markgo:1.0.1
echo "生成docker 镜像：z_markgo:1.0.1！"
rm -rf ../z_markgo_cp
echo "删除临时文件z_markgo_cp！"
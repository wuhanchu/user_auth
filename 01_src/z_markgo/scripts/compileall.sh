#复制代码到
echo "复制代码到../z_margo_cp"
cp ../z_markgo ../z_margo_cp
cd ../z_margo_cp
find -name "__pycache__" -exec rm -rf {} \;
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
find -name "__pycache__" -exec rm -rf {} \;
find -name "*.py" -exec rm -rf {} \;
echo "代码编译完成！"
echo "开始生成docker 镜像！"
docker build . -t z_markgo:1.0.2
echo "生成docker 镜像：z_markgo:1.0.2！"

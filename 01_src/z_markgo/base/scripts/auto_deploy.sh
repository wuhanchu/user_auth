#项目自动部署
set -e
echo "更新git 代码"
git pull
echo "启动项目"
sh service.sh restart
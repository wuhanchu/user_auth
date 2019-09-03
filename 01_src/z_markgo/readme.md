# 项目标注狗

## 框架说明：
1. config.py 数据库，日志等相关配置信息
2. webapi目录：接口相关文件所在目录，
3. webapi/__init__.py: 所有接口的路径应以/api/v*/ 为前缀，所以接口的写法应通过__init__.py中定义的Blueprint的路由进行访问，可自己新增Blueprint定义
4. lib/models.py :orm模型文件（可以通过sqlacodegen自动生成models文件）
5. lib/JsonResult.py : 标准的返回格式，所有接口的返回都通过这个处理方法。

## 部署

- 编译docker镜像: `docker build . -t z_markgo`
- 运行docker容器:

```docker
docker run -d -p 15002:5002 --name z_marlgo_1 -e SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@dataknown.tpddns.cn:503 06/z_markgo?charset=utf8" -v ~/tmp/z_markgo_items:/opt/z_markgo_items z_markgo

- SQLALCHEMY_DATABASE_URI 数据库链接URL
- /opt/z_markgo_items 是文件的上传路径，需要映射到宿主机，例子中映射到了 ～/tmp/z_markgo_items
- 5002是运行接口，宿主机15002绑定到容器的5002
- 运行镜像z_markgo
- 容器名为z_marlgo_1
```

- 导出镜像：docker save ‒o z_markgo.docker z_markgo
- 导入镜像：docker load ‒‒input z_markgo.docker

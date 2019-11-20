# docker部署

- 编译docker镜像: `docker build . -t z_markgo`
- 运行docker容器:

```docker
docker run -d -p 5002:5002 --name z_markgo -e SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@192.168.1.150:3306/z_markgo?charset=utf8' -v ~/tmp/z_markgo_items:/opt/z_markgo_items z_markgo:1.0.1

- SQLALCHEMY_DATABASE_URI 数据库链接URL
- /opt/z_markgo_items 是文件的上传路径，需要映射到宿主机，例子中映射到了 ～/tmp/z_markgo_items
- 5002是运行接口，宿主机15002绑定到容器的5002
- 运行镜像z_markgo
- 容器名为z_marlgo_1
```

- 导出镜像：docker save -o ./z_markgo.docker z_markgo
- 导入镜像：docker load ‒‒input z_markgo.docker

# 项目标注狗

## 框架说明：
1. config.py 数据库，日志等相关配置信息
2. webapi目录：接口相关文件所在目录，
3. webapi/__init__.py: 所有接口的路径应以/api/v*/ 为前缀，所以接口的写法应通过__init__.py中定义的Blueprint的路由进行访问，可自己新增Blueprint定义
4. lib/models.py :orm模型文件（可以通过sqlacodegen自动生成models文件）
5. lib/JsonResult.py : 标准的返回格式，所有接口的返回都通过这个处理方法。



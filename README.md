# flask 通用授权项目

## 注意事项

oauth2_client 的元数据生效的是 client_metadata

`{"grant_types": ["authorization_code","password"], "response_types":"code", "scope":"profile"}`

grant_type
response_type
scope
并没有生效
git

### 环境要求

1. Python 3.8+

## 环境变量

| 分组                   | 配置项                                                  | 说明                                                            |
| ---------------------- | ------------------------------------------------------- | --------------------------------------------------------------- |
| 数据库                 | SQLALCHEMY_DATABASE_URI                                 | 数据库链接地址                                                  |
| 数据库                 | DB_SCHEMA                                               | 对接的数据库 schema                                             |
| 数据库                 | AUTO_UPDATE                                             | 是否自动更新数据库(DB_INIT_FILE,DB_VERSION_FILE,DB_UPDATE_FILE) |
| 数据库                 | DB_INIT_FILE                                            | 数据库初始化脚本                                                |
| 数据库                 | DB_VERSION_FILE                                         | 数据库迭代脚本（根据版本更新）                                  |
| 数据库                 | DB_UPDATE_FILE                                          | 数据库开发脚本（本次启动运行）                                  |
| 数据库                 | PROXY_SERVER_URL                                        | 代理请求地址                                                    |
| 权限                   | FETCH_USER                                              | 是否获取用户                                                    |
| 权限                   | CHECK_API                                               | API 接口检查                                                    |
| 权限 ｜ CHECK_PASSWORD | 是否检查用户密码，还是只需要检查用户账号。（默认是） ｜ |
| 缓存                   | REDIS_URL                                               | redis 地址                                                      |
| 缓存                   | REDIS_MASTER_NAME                                       | redis master name                                               |

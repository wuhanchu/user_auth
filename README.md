# flask 通用授权项目

## 注意事项

oauth2_client 的元数据生效的是client_metadata

`{"grant_types": ["authorization_code","password"], "response_types":"code", "scope":"profile"}`

grant_type
response_type
scope
并没有生效
git


## 数据库初始化

- 创建对应的数据库实例和schema(user_auth)
- 执行init数据库脚本

1. table.sql
2. view.sql
3. data
   1. permission.sql
      permission_scope.sql
      role.sql
      user.sql
   2. user_role.sql
      role_permission_scope.sql
      permission_scope_detail.sql
   3. param.sql
      
默认admin的密码是 dataknown1234

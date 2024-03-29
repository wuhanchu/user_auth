DELETE
FROM
    user_auth.permission_scope
WHERE
        product_key = 'user_auth';

INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '登录', 'login', NULL, 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '系统管理', 'system', 'login', 'user_auth' );
-- 证书
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '证书', 'license', 'system', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '证书_校验', 'license_check_get', 'license', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '证书_构造', 'license_file_post', 'license', 'user_auth' );

-- 角色
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '角色', 'role_get', 'system', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '角色_删除', 'role_delete', 'role_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '角色_修改', 'role_patch', 'role_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '角色_新增', 'role_post', 'role_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '角色_导出', 'role_export', 'role_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '角色_导入', 'role_import', 'role_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '角色_权限', 'role_permission_get', 'role_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '角色_功能_查询', 'role_permission_scope_get', 'role_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '角色_功能_覆盖', 'role_permission_scope_put', 'role_get', 'user_auth' );

-- 用户
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '用户', 'user_get', 'system', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '用户_删除', 'user_delete', 'user_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '用户_修改', 'user_patch', 'user_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '用户_新增', 'user_post', 'user_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '分配角色', 'user_role_put', 'user_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '用户_导出', 'user_export', 'user_get', 'user_auth' );

-- 部门
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '部门', 'department_get', 'system', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '部门_删除', 'department_delete', 'department_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '部门_导出', 'department_export', 'department_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '部门_导入', 'department_import', 'department_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '部门_修改', 'department_patch', 'department_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '部门_新增', 'department_post', 'department_get', 'user_auth' );

-- 客户端
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '客户端', 'oauth2_client_get', 'system', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '客户端_删除', 'oauth2_client_delete', 'oauth2_client_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '客户端_导出', 'oauth2_client_export', 'oauth2_client_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '客户端_导入', 'oauth2_client_import', 'oauth2_client_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '客户端_修改', 'oauth2_client_patch', 'oauth2_client_get', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '客户端_新增', 'oauth2_client_post', 'oauth2_client_get', 'user_auth' );

-- 配置
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '配置', 'config_get', 'system', 'user_auth' );
INSERT INTO user_auth.permission_scope ( "name", "key", "parent_key", "product_key" )
VALUES
    ( '配置_修改', 'config_patch', 'config_get', 'user_auth' );
DELETE 
FROM
	user_auth.permission 
WHERE
	product_key = "user_auth";
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/authorize', 'GET', 'auth_authorize_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/authorize', 'POST', 'auth_authorize_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/create_client', 'GET', 'auth_create_client_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/create_client', 'POST', 'auth_create_client_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/', 'GET', 'auth_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_登出', NULL, '/auth/logout', 'GET', 'auth_logout_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/', 'POST', 'auth_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/revoke', 'POST', 'auth_revoke_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_登录', NULL, '/auth/token', 'POST', 'auth_token_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '证书_校验', NULL, '/license/check', 'GET', 'license_check_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '证书_构造', NULL, '/license/file', 'POST', 'license_file_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '证书_查询', NULL, '/license', 'GET', 'license_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '证书_上传', NULL, '/license', 'POST', 'license_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '客户端_删除', NULL, '/oauth2_client', 'DELETE', 'oauth2_client_delete', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '客户端_查询', NULL, '/oauth2_client', 'GET', 'oauth2_client_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '客户端_修改', NULL, '/oauth2_client', 'PATCH', 'oauth2_client_patch', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '客户端_新增', NULL, '/oauth2_client', 'POST', 'oauth2_client_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '客户端_覆盖', NULL, '/oauth2_client', 'PUT', 'oauth2_client_put', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '接口_删除', NULL, '/permission', 'DELETE', 'permission_delete', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '接口_查询', NULL, '/permission', 'GET', 'permission_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '接口_修改', NULL, '/permission', 'PATCH', 'permission_patch', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '接口_新增', NULL, '/permission', 'POST', 'permission_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '接口_覆盖', NULL, '/permission', 'PUT', 'permission_put', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '功能_删除', NULL, '/permission_scope', 'DELETE', 'permission_scope_delete', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '功能_查询', NULL, '/permission_scope', 'GET', 'permission_scope_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '功能_修改', NULL, '/permission_scope', 'PATCH', 'permission_scope_patch', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '角色_查询', NULL, '/role', 'GET', 'role_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '功能_新增', NULL, '/permission_scope', 'POST', 'permission_scope_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '功能_覆盖', NULL, '/permission_scope', 'PUT', 'permission_scope_put', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '角色_删除', NULL, '/role', 'DELETE', 'role_delete', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '角色_修改', NULL, '/role', 'PATCH', 'role_patch', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '角色_权限_查询', NULL, '/role/permission', 'GET', 'role_permission_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '角色_功能_查询', NULL, '/role/permission_scope', 'GET', 'role_permission_scope_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '角色_功能_覆盖', NULL, '/role/permission_scope', 'PUT', 'role_permission_scope_put', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '角色_新增', NULL, '/role', 'POST', 'role_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '角色_覆盖', NULL, '/role', 'PUT', 'role_put', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_当前', NULL, '/user/current', 'GET', 'user_current_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_删除', NULL, '/user', 'DELETE', 'user_delete', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_查询', NULL, '/user', 'GET', 'user_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_密码_修改', NULL, '/user/password', 'PUT', 'user_password_put', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_修改', NULL, '/user', 'PATCH', 'user_patch', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_新增', NULL, '/user', 'POST', 'user_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_覆盖', NULL, '/user', 'PUT', 'user_put', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_角色_获取', NULL, '/user/role', 'GET', 'user_role_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '用户_角色_覆盖', NULL, '/user/role', 'PUT', 'user_role_put', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/', 'GET', 'auth__get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/', 'POST', 'auth__post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/auth/token', 'DELETE', 'auth_token_delete', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/debug-sentry', 'GET', 'debug-sentry_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '部门_删除', NULL, '/department', 'DELETE', 'department_delete', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '部门_查询', NULL, '/department', 'GET', 'department_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '部门_修改', NULL, '/department', 'PATCH', 'department_patch', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '部门_新增', NULL, '/department', 'POST', 'department_post', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( '部门_覆盖', NULL, '/department', 'PUT', 'department_put', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/static/<path:filename>', 'GET', 'static_<path:filename>_get', 'user_auth' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/debug-sentry', 'GET', 'debug-sentry_get', 'z_ai_service' );
INSERT INTO "permission" ( "name", "description", "url", "method", "key", "product_key" )
VALUES
	( NULL, NULL, '/static/<path:filename>', 'GET', 'static_<path:filename>_get', 'z_ai_service' );
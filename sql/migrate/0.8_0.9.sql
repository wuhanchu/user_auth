ALTER TABLE "user_auth"."role_permission_scope"
    DROP CONSTRAINT if exists "role_permission_scope_permission_scope_product_key_key_fk";

delete
from "permission_scope"
where product_key = 'user_auth';

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('登录', 'login', NULL, 'user_auth')
ON CONFLICT DO NOTHING;


INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('系统管理', 'system', 'login', 'user_auth')
ON CONFLICT DO NOTHING;


INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('证书', 'license', 'system', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('证书_校验', 'license_check_get', 'license', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('证书_构造', 'license_file_post', 'license', 'user_auth')
ON CONFLICT DO NOTHING;


INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('角色', 'role_get', 'system', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('角色_删除', 'role_delete', 'role_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('角色_修改', 'role_patch', 'role_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('角色_新增', 'role_post', 'role_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('角色_导出', 'role_export', 'role_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('角色_导入', 'role_import', 'role_get', 'user_auth')
ON CONFLICT DO NOTHING;


INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('角色_权限', 'role_permission_get', 'role_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('角色_功能_查询', 'role_permission_scope_get', 'role_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('角色_功能_覆盖', 'role_permission_scope_put', 'role_get', 'user_auth')
ON CONFLICT DO NOTHING;


INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('用户', 'user_get', 'system', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('用户_删除', 'user_delete', 'user_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('用户_修改', 'user_patch', 'user_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('用户_新增', 'user_post', 'user_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('分配角色', 'user_role_put', 'user_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('用户_导出', 'user_export', 'user_get', 'user_auth')
ON CONFLICT DO NOTHING;


INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('部门', 'department_get', 'system', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('部门_删除', 'department_delete', 'department_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('部门_导出', 'department_export', 'department_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('部门_导入', 'department_import', 'department_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('部门_修改', 'department_patch', 'department_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('部门_新增', 'department_post', 'department_get', 'user_auth')
ON CONFLICT DO NOTHING;


INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('客户端', 'oauth2_client_get', 'system', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('客户端_删除', 'oauth2_client_delete', 'oauth2_client_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('客户端_导出', 'oauth2_client_export', 'oauth2_client_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('客户端_导入', 'oauth2_client_import', 'oauth2_client_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('客户端_修改', 'oauth2_client_patch', 'oauth2_client_get', 'user_auth')
ON CONFLICT DO NOTHING;

INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key")
VALUES ('客户端_新增', 'oauth2_client_post', 'oauth2_client_get', 'user_auth')
ON CONFLICT DO NOTHING;

insert into role_permission_scope(role_id, permission_scope_key, product_key)
select 1 as role_id, key as permission_scope_key, product_key
from permission_scope
where (product_key, key) not in (select product_key, permission_scope_key from role_permission_scope where role_id = 1);


UPDATE "param"
SET name  = '版本',
    value = '0.9'
WHERE key = 'version';

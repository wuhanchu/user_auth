-- 清理无效的权限信息

delete
from user_auth.permission_scope_detail
where product_key is null
   or product_key not in (SELECT schema_name
                          FROM information_schema.schemata);
delete
from user_auth.permission_scope
where product_key is null
   or product_key not in (SELECT schema_name
                          FROM information_schema.schemata);


delete
from user_auth.permission
where product_key is null
   or product_key not in (SELECT schema_name
                          FROM information_schema.schemata);

delete
from user_auth.role_permission_scope
where product_key is null
   or product_key not in (SELECT schema_name
                          FROM information_schema.schemata);

UPDATE
    "param"
SET value = '0.12.2'
WHERE key = 'version';
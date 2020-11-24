insert into role_permission_scope(role_id, permission_scope_key, product_key)
select 1 as role_id, key as permission_scope_key, product_key
from permission_scope
where (product_key, key) not in (select product_key, permission_scope_key from role_permission_scope where role_id = 1);

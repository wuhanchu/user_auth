drop view IF EXISTS permission_role cascade;

drop view IF EXISTS user_extend cascade;

-- 角色权限
create or replace view permission_role as
SELECT permission.name,
       permission.url,
       permission.method,
       string_agg(role.id :: text, ',' :: text)   AS role_ids,
       string_agg(role.name :: text, ',' :: text) AS role_names
FROM permission
         JOIN permission_scope_detail ON permission_scope_detail.permission_key :: text = permission.key :: text
         JOIN permission_scope ON permission_scope.key :: text = permission_scope_detail.permission_scope_key :: text
         JOIN role_permission_scope ON role_permission_scope.permission_scope_key :: text = permission_scope.key :: text
         JOIN role ON role.id = role_permission_scope.role_id
GROUP BY permission.name,
         permission.url,
         permission.method;

-- 用户角色
create or replace view user_extend as
select "user".id,
       "user".loginid,
       "user".name,
       "user".enable,
       "user".department_key,
       "user".address,
       "user".email,
       "user".mobile_phone,
       "user".telephone,
       "user".remark,
       "user".create_time,
       "user".update_time,
       array_agg(ur.role_id) filter (
           where
           ur.role_id is not null
           ) as role_id
from "user"
         left join user_role ur on "user".id = ur.user_id
group by "user".id;
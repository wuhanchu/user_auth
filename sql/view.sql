drop view IF EXISTS permission_role;

create or replace view permission_role(name, url, method, role_ids, role_names) as
SELECT permission.name,
       permission.url,
       permission.method,
       string_agg(role.id::text, ','::text)   AS role_ids,
       string_agg(role.name::text, ','::text) AS role_names
FROM permission
         JOIN permission_scope_detail ON permission_scope_detail.permission_key::text = permission.key::text
         JOIN permission_scope ON permission_scope.key::text = permission_scope_detail.permission_scope_key::text
         JOIN role_permission_scope ON role_permission_scope.permission_scope_key::text = permission_scope.key::text
         JOIN role ON role.id = role_permission_scope.role_id
GROUP BY permission.name, permission.url, permission.method;

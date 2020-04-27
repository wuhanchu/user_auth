-- 设置路径
set search_path to user_auth;

-- 权限配置
select t.name, sp.name, sp.url, sp.method
from permission_scope t
         join permission_scope_detail t1 on t.key = t1.permission_scope_key
         left join permission sp on t1.permission_key = sp.key
order by t.name;


-- 重复权限
select *
from permission
where (product_key, key) in (select product_key, permission_key from permission_scope_detail)
  and (product_key, key) in (select product_key, key
                             from permission
                             group by product_key, key
                             having count(*) > 1
);

-- 重复权限配置
select *
from permission_scope_detail
where (product_key, permission_key) in (
    select product_key, key
    from permission
    where (product_key, key) in (select product_key, permission_key from permission_scope_detail)
      and (product_key, key) in (select product_key, key
                                 from permission
                                 group by product_key, key
                                 having count(*) > 1
    ));

-- 插入缺少的功能
insert into permission_scope(key, name, product_key)
select key, name, product_key
from permission
where product_key = 'user_auth'
  and key not in (select key from permission_scope);


-- 查看没有配置权限的功能
select *
from permission_scope
where (product_key, key) not in (select product_key, permission_scope_key from permission_scope_detail);

-- 插入功能缺少的权限配置
insert into permission_scope_detail(product_key, permission_key, permission_scope_key, product_key)
select product_key, key as permission_key, key as permission_scope_key, product_key
from permission_scope
where (product_key, key) not in (select product_key, permission_scope_key from permission_scope_detail)
  and (product_key, key) in (select product_key, key from permission);

-- 给 sysadmin 授权所有
insert into role_permission_scope(role_id, permission_scope_key, product_key)
select 1 as role_id, key as permission_scope_key, product_key
from permission_scope
where (product_key, key) not in (select product_key, permission_scope_key from role_permission_scope where role_id = 1);


-- 查看配置了多个权限的功能
select *
from permission_scope
         left join permission_scope_detail on permission_scope.product_key = permission_scope_detail.product_key and
                                              permission_scope.key = permission_scope_detail.permission_scope_key
where (permission_scope_detail.product_key, permission_scope.key) in
      (select product_key
            , permission_scope_key
       from permission_scope_detail
       group by product_key
              , permission_scope_key
       having count(id)
                  > 1);

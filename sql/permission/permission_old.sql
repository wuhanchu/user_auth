select *
from sys_permission_group_rel;

select sys_permission_group.id,
       sys_permission_group.key,
       sys_permission_group.group_name,
       sys_permission.id,
       sys_permission.name,
       sys_permission.url,
       sys_permission.method
from sys_permission_group
         left join sys_permission_group_rel on sys_permission_group.id = sys_permission_group_rel.permission_group_id
         left join sys_permission on sys_permission.id = sys_permission_group_rel.permission_id
where sys_permission_group.id in (select permission_group_id
                                  from sys_permission_group_rel
                                  group by permission_group_id
                                  having count(id) > 1)

order by sys_permission_group.id;
INSERT INTO department (name, key)
VALUES ('顶级部门', 'top')
on conflict do nothing;
-- 创建临时表
CREATE temp TABLE role_temp (
    id integer,
    name varchar(64) not null,
    chinese_name varchar(64),
    description varchar(255),
    opr_by varchar(32),
    opr_at bigint,
    del_fg smallint,
    remark text
);
-- 具体数据
truncate TABLE role_temp;

INSERT INTO role_temp (name, chinese_name, description)
VALUES ('superadmin', '超级管理员', '超管');

-- 新增数据
INSERT INTO user_auth.role(name, chinese_name, description)
SELECT name,
    chinese_name,
    description
FROM role_temp
WHERE role_temp.name not IN (
        SELECT "name"
        FROM user_auth.role
    );
-- 更新角色
update user_auth.role
SET chinese_name = role_temp.chinese_name,
    description = role_temp.description
FROM role_temp
WHERE role_temp.name = user_auth.role.name;
-- 清空
truncate TABLE role_temp;
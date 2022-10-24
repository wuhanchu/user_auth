-- 创建临时表
create temp table if not exists config_temp
(
    key    text not null
        constraint config_pk
            primary key,
    name   text,
    value  text,
    remark text
);
truncate table config_temp;

-- 数据
INSERT INTO "config_temp"("key", "name", "value", "remark")
VALUES ('register_switch', '注册开关', 'false', '登陆界面是否开启用户注册');


-- 更新
insert into config
select key, name, value, remark
from config_temp
where config_temp.key not in (select "key" from config);

update config
set name   = config_temp.name,
    remark = config_temp.remark
from config_temp
where config_temp.key = config.key;

truncate table config_temp;
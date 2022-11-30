

create sequence user_auth.department_id_seq;



create sequence user_auth.oauth2_client_id_seq;



create sequence user_auth.oauth2_code_id_seq;



create sequence user_auth.oauth2_token_id_seq;



create sequence user_auth.permission_scope_detail_id_seq;



create sequence user_auth.role_id_seq;



CREATE SEQUENCE  user_auth.role_permission_scope_id_seq start 1000;


create sequence user_auth.sys_user_role_id_seq
    maxvalue 2147483647;



create sequence user_auth.user_id_seq;

create sequence user_auth.weixin_id_seq
    maxvalue 2147483647;



create sequence user_auth.config_id_seq
    maxvalue 2147483647;



create table user_auth.department
(
    id          integer      default nextval('user_auth.department_id_seq'::regclass) not null
        constraint department_pk
            primary key,
    name        varchar(255)                                                          not null,
    key         text                                                                  not null,
    create_time timestamp(6) default CURRENT_TIMESTAMP,
    update_time timestamp(6),
    external_id varchar(256),
    source      varchar(64),
    remark      text,
    order_no    integer,
    constraint department_pk_2
        unique (source, external_id)
);

comment on table user_auth.department is '部门表';

comment on column user_auth.department.key is '编码';

comment on column user_auth.department.external_id is '外部 ID';

comment on column user_auth.department.source is '来源';

comment on column user_auth.department.order_no is '排序号';



alter sequence user_auth.department_id_seq owned by user_auth.department.id;

create unique index department_key_uindex
    on user_auth.department (key);

create unique index department_name_uindex
    on user_auth.department (name);

create table user_auth.license
(
    product_key text not null
        constraint license_pk
            primary key,
    content     text not null
);

comment on column user_auth.license.product_key is '项目KEY';

comment on column user_auth.license.content is '证书内容';



create unique index license_product_key_uindex
    on user_auth.license (product_key);

create table user_auth.param
(
    name  text,
    key   text not null
        constraint param_pk
            primary key,
    value text
);



create unique index param_key_uindex
    on user_auth.param (key);

create table user_auth.permission
(
    name        varchar(64),
    description varchar(255),
    url         varchar(64),
    method      varchar(50),
    key         varchar(64) not null,
    product_key text        not null,
    constraint permission_pk
        primary key (product_key, key)
);

comment on table user_auth.permission is '系统权限表';

comment on column user_auth.permission.name is '权限名称';

comment on column user_auth.permission.description is '权限描述';

comment on column user_auth.permission.url is '路由匹配地址';

comment on column user_auth.permission.method is '1，get，2.post，3.put；4，delete';



create table user_auth.permission_scope
(
    name        varchar(255),
    key         varchar(255) not null,
    parent_key  varchar(255),
    product_key text         not null,
    constraint permission_scope_pk
        primary key (product_key, key)
);

comment on column user_auth.permission_scope.key is '关联菜单字段';

comment on column user_auth.permission_scope.parent_key is '父节点';



create table user_auth.permission_scope_detail
(
    permission_key       varchar(255),
    permission_scope_key varchar(255),
    id                   integer default nextval('user_auth.permission_scope_detail_id_seq'::regclass) not null
        primary key,
    product_key          text,
    product_key_scope    text,
    constraint permission_scope_detail_permission_key_product_key_fk
        foreign key (permission_key, product_key) references user_auth.permission (key, product_key),
    constraint permission_scope_detail_permission_scope_key_product_key_fk
        foreign key (permission_scope_key, product_key_scope) references user_auth.permission_scope (key, product_key)
);



alter sequence user_auth.permission_scope_detail_id_seq owned by user_auth.permission_scope_detail.product_key_scope;

create index fk_perssion_id
    on user_auth.permission_scope_detail (permission_key);

create table user_auth.role
(
    id           integer default nextval('user_auth.role_id_seq'::regclass) not null
        constraint sys_role_pkey
            primary key,
    name         varchar(64)                                                not null,
    chinese_name varchar(64),
    description  varchar(255),
    opr_by       varchar(32),
    opr_at       bigint,
    del_fg       smallint,
    remark       text
);

comment on table user_auth.role is '角色表';

comment on column user_auth.role.id is '角色ID';

comment on column user_auth.role.name is '角色名称';

comment on column user_auth.role.chinese_name is '角色中文名';

comment on column user_auth.role.description is '角色描述';

comment on column user_auth.role.opr_by is '操作人';

comment on column user_auth.role.opr_at is '操作时间';

comment on column user_auth.role.del_fg is '删除标识';



alter sequence user_auth.role_id_seq owned by user_auth.role.id;

create unique index role_chinese_name_uindex
    on user_auth.role (chinese_name);

create unique index role_name_uindex
    on user_auth.role (name);

create table user_auth.role_permission_scope
(
    role_id              integer                                                                     not null
        constraint role_permission_scope_role_id_fk
            references user_auth.role
            on update cascade on delete cascade,
    permission_scope_key varchar                                                                     not null,
    id                   integer default nextval('user_auth.role_permission_scope_id_seq'::regclass) not null
        constraint role_permission_scope_pk
            primary key,
    product_key          text
);

comment on table user_auth.role_permission_scope is '权限角色表
';



alter sequence user_auth.role_permission_scope_id_seq owned by user_auth.role_permission_scope.id;

create unique index role_permission_scope_id_uindex
    on user_auth.role_permission_scope (id);

create table user_auth."user"
(
    id             integer      default nextval('user_auth.user_id_seq'::regclass) not null
        constraint sys_user_pkey
            primary key,
    name           varchar(32)                                                     not null,
    telephone      varchar(16),
    address        varchar(64),
    loginid        varchar(255),
    password       varchar(255),
    token          varchar(100),
    expires_in     integer,
    login_at       bigint,
    login_ip       varchar(100),
    login_count    integer      default 0,
    remark         text,
    opr_by         varchar(32),
    opr_at         bigint,
    del_fg         smallint,
    department_key text[],
    external_id    varchar(255),
    source         varchar(64),
    email          varchar(255),
    mobile_phone   varchar(255),
    create_time    timestamp(6) default CURRENT_TIMESTAMP,
    update_time    timestamp(6),
    enable         boolean      default true,
    constraint external_pk
        unique (source, external_id)
);

comment on table user_auth."user" is '用户表';

comment on column user_auth."user".id is '用户ID';

comment on column user_auth."user".name is '用户姓名';

comment on column user_auth."user".telephone is '用户电话';

comment on column user_auth."user".address is '用户地址';

comment on column user_auth."user".loginid is '用户名';

comment on column user_auth."user".password is '用户密码';

comment on column user_auth."user".token is '访问凭证';

comment on column user_auth."user".expires_in is '凭证有效期';

comment on column user_auth."user".login_at is '登录时间';

comment on column user_auth."user".login_ip is '登录IP';

comment on column user_auth."user".login_count is '登录次数';

comment on column user_auth."user".remark is '备注';

comment on column user_auth."user".opr_by is '操作人';

comment on column user_auth."user".opr_at is '操作时间';

comment on column user_auth."user".del_fg is '1：已删除 0：未删除';

comment on column user_auth."user".department_key is '部门编码';

comment on column user_auth."user".external_id is '外部 ID';

comment on column user_auth."user".source is '数据来源';

comment on column user_auth."user".email is '邮件';

comment on column user_auth."user".mobile_phone is '用户手机';

comment on column user_auth."user".enable is '是否启用';



alter sequence user_auth.user_id_seq owned by user_auth."user".id;

create table user_auth.oauth2_client
(
    client_id                  varchar(48),
    client_secret              varchar(120),
    client_id_issued_at        integer,
    client_secret_expires_at   integer,
    redirect_uri               text,
    token_endpoint_auth_method varchar(48),
    grant_type                 text                                                                not null,
    response_type              text                                                                not null,
    scope                      text                                                                not null,
    client_name                varchar(100),
    client_uri                 text,
    logo_uri                   text,
    contact                    text,
    tos_uri                    text,
    policy_uri                 text,
    jwks_uri                   text,
    jwks_text                  text,
    i18n_metadata              text,
    software_id                varchar(36),
    software_version           varchar(48),
    id                         integer default nextval('user_auth.oauth2_client_id_seq'::regclass) not null
        primary key,
    user_id                    integer
                                                                                                   references user_auth."user"
                                                                                                       on delete set null,
    client_metadata            json,
    issued_at                  integer,
    expires_at                 integer
);



alter sequence user_auth.oauth2_client_id_seq owned by user_auth.oauth2_client.id;

create index ix_oauth2_client_client_id
    on user_auth.oauth2_client (client_id);

create index user_id
    on user_auth.oauth2_client (user_id);

create table user_auth.oauth2_code
(
    code           varchar(120)                                                      not null
        unique,
    client_id      varchar(48),
    redirect_uri   text,
    response_type  text,
    scope          text,
    auth_time      integer                                                           not null,
    id             integer default nextval('user_auth.oauth2_code_id_seq'::regclass) not null
        primary key,
    user_id        integer
        references user_auth."user"
            on update cascade on delete cascade,
    code_challenge text    default 'test'::text
);



alter sequence user_auth.oauth2_code_id_seq owned by user_auth.oauth2_code.id;

create index code
    on user_auth.oauth2_code (code);

create table user_auth.oauth2_token
(
    client_id     varchar(48),
    token_type    varchar(40),
    access_token  varchar(255)                                                       not null
        unique,
    refresh_token varchar(255),
    scope         text,
    issued_at     integer                                                            not null,
    expires_in    integer                                                            not null,
    id            integer default nextval('user_auth.oauth2_token_id_seq'::regclass) not null
        primary key,
    user_id       integer
        references user_auth."user"
            on update cascade on delete cascade,
    revoked       boolean
);



alter sequence user_auth.oauth2_token_id_seq owned by user_auth.oauth2_token.id;

create index access_token
    on user_auth.oauth2_token (access_token);

create index ix_oauth2_token_refresh_token
    on user_auth.oauth2_token (refresh_token);

create index ix_test_oauth2_token_refresh_token
    on user_auth.oauth2_token (refresh_token);

create unique index "username_UNIQUE"
    on user_auth."user" (loginid);

comment on index user_auth."username_UNIQUE" is '用户名唯一';

create table user_auth.user_role
(
    id      integer default nextval('user_auth.sys_user_role_id_seq'::regclass) not null
        primary key,
    user_id integer
        constraint user_role_user_id_fk
            references user_auth."user"
            on update cascade on delete cascade,
    role_id integer
        constraint sys_user_role_role_id_fk
            references user_auth.role
            on update cascade on delete cascade
);

comment on table user_auth.user_role is '用户角色表';



alter sequence user_auth.sys_user_role_id_seq owned by user_auth.user_role.id;

create table user_auth.weixin
(
    id         integer     default nextval('user_auth.weixin_id_seq'::regclass) not null
        primary key,
    name       varchar(32)                                                      not null,
    openid     varchar(128),
    createtime timestamp(6),
    updatetime timestamp(6),
    sex        varchar(8),
    province   varchar(16),
    city       varchar(56),
    country    varchar(128),
    headimgurl varchar(16),
    unionid    varchar(32) default ''::character varying
);



alter sequence user_auth.weixin_id_seq owned by user_auth.weixin.id;

create table user_auth.config
(
    key    text                                                         not null,
    name   text,
    value  text,
    remark text,
    id     integer default nextval('user_auth.config_id_seq'::regclass) not null
        primary key
);

comment on table user_auth.config is '配置';

comment on column user_auth.config.key is '名称';

comment on column user_auth.config.remark is '备注';



alter sequence user_auth.config_id_seq owned by user_auth.config.id;


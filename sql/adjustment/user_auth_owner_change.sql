-- schame对象修改
set search_path to user_auth;

alter table
    department
    owner to dataknown;

alter table
    license
    owner to dataknown;

alter table
    param
    owner to dataknown;

alter table
    permission
    owner to dataknown;

alter table
    permission_scope
    owner to dataknown;

alter table
    permission_scope_detail
    owner to dataknown;

alter table
    role
    owner to dataknown;

alter table
    role_permission_scope
    owner to dataknown;

alter table
    "user"
    owner to dataknown;

alter table
    oauth2_client
    owner to dataknown;

alter table
    oauth2_code
    owner to dataknown;

alter table
    oauth2_token
    owner to dataknown;

alter table
    user_role
    owner to dataknown;

alter table
    weixin
    owner to dataknown;

alter view
    permission_role
    owner to dataknown;

alter view
    user_extend
    owner to dataknown;

alter sequence department_id_seq owner to dataknown;

alter sequence oauth2_client_id_seq owner to dataknown;

alter sequence oauth2_code_id_seq owner to dataknown;

alter sequence oauth2_token_id_seq owner to dataknown;

alter sequence permission_scope_detail_id_seq owner to dataknown;

alter sequence role_id_seq owner to dataknown;

alter sequence role_permission_scope_id_seq owner to dataknown;

alter sequence sys_user_role_id_seq owner to dataknown;

alter sequence user_id_seq owner to dataknown;

alter sequence weixin_id_seq owner to dataknown;
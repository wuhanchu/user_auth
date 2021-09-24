/*
 Navicat Premium Data Transfer

 Source Server         : dataknown_postgres_dev
 Source Server Type    : PostgreSQL
 Source Server Version : 120004
 Source Host           : server.aiknown.cn:32021
 Source Catalog        : dataknown
 Source Schema         : user_auth

 Target Server Type    : PostgreSQL
 Target Server Version : 120004
 File Encoding         : 65001

 Date: 24/11/2020 10:58:55
*/


-- ----------------------------
-- Sequence structure for department_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "department_id_seq";
CREATE SEQUENCE "department_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;

-- ----------------------------
-- Sequence structure for oauth2_client_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "oauth2_client_id_seq";
CREATE SEQUENCE "oauth2_client_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;

-- ----------------------------
-- Sequence structure for oauth2_code_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "oauth2_code_id_seq";
CREATE SEQUENCE "oauth2_code_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;

-- ----------------------------
-- Sequence structure for oauth2_token_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "oauth2_token_id_seq";
CREATE SEQUENCE "oauth2_token_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;

-- ----------------------------
-- Sequence structure for permission_scope_detail_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "permission_scope_detail_id_seq";
CREATE SEQUENCE "permission_scope_detail_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;

-- ----------------------------
-- Sequence structure for role_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "role_id_seq";
CREATE SEQUENCE "role_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;

-- ----------------------------
-- Sequence structure for role_permission_scope_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "role_permission_scope_id_seq";
CREATE SEQUENCE "role_permission_scope_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1000
    CACHE 1;

-- ----------------------------
-- Sequence structure for sys_user_role_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "sys_user_role_id_seq";
CREATE SEQUENCE "sys_user_role_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 2147483647
    START 1
    CACHE 1;

-- ----------------------------
-- Sequence structure for user_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_id_seq";
CREATE SEQUENCE "user_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;

-- ----------------------------
-- Sequence structure for weixin_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "weixin_id_seq";
CREATE SEQUENCE "weixin_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 2147483647
    START 1
    CACHE 1;

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS "department";
CREATE TABLE "department" (
                                          "id" int4 NOT NULL DEFAULT nextval('department_id_seq'::regclass),
                                          "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
                                          "key" text COLLATE "pg_catalog"."default" NOT NULL,
                                          "create_time" timestamp(6) DEFAULT CURRENT_TIMESTAMP,
                                          "update_time" timestamp(6),
                                          "external_id" varchar(256) COLLATE "pg_catalog"."default",
                                          "source" varchar(64) COLLATE "pg_catalog"."default",
                                          "remark" text COLLATE "pg_catalog"."default",
                                          "order_no" int4
)
;
COMMENT ON COLUMN "department"."key" IS '编码';
COMMENT ON COLUMN "department"."external_id" IS '外部 ID';
COMMENT ON COLUMN "department"."source" IS '来源';
COMMENT ON COLUMN "department"."order_no" IS '排序号';
COMMENT ON TABLE "department" IS '部门表';

-- ----------------------------
-- Table structure for license
-- ----------------------------
DROP TABLE IF EXISTS "license";
CREATE TABLE "license" (
                                       "product_key" text COLLATE "pg_catalog"."default" NOT NULL,
                                       "content" text COLLATE "pg_catalog"."default" NOT NULL
)
;
COMMENT ON COLUMN "license"."product_key" IS '项目KEY';
COMMENT ON COLUMN "license"."content" IS '证书内容';

-- ----------------------------
-- Table structure for oauth2_client
-- ----------------------------
DROP TABLE IF EXISTS "oauth2_client";
CREATE TABLE "oauth2_client" (
                                             "client_id" varchar(48) COLLATE "pg_catalog"."default",
                                             "client_secret" varchar(120) COLLATE "pg_catalog"."default",
                                             "client_id_issued_at" int4,
                                             "client_secret_expires_at" int4,
                                             "redirect_uri" text COLLATE "pg_catalog"."default",
                                             "token_endpoint_auth_method" varchar(48) COLLATE "pg_catalog"."default",
                                             "grant_type" text COLLATE "pg_catalog"."default" NOT NULL,
                                             "response_type" text COLLATE "pg_catalog"."default" NOT NULL,
                                             "scope" text COLLATE "pg_catalog"."default" NOT NULL,
                                             "client_name" varchar(100) COLLATE "pg_catalog"."default",
                                             "client_uri" text COLLATE "pg_catalog"."default",
                                             "logo_uri" text COLLATE "pg_catalog"."default",
                                             "contact" text COLLATE "pg_catalog"."default",
                                             "tos_uri" text COLLATE "pg_catalog"."default",
                                             "policy_uri" text COLLATE "pg_catalog"."default",
                                             "jwks_uri" text COLLATE "pg_catalog"."default",
                                             "jwks_text" text COLLATE "pg_catalog"."default",
                                             "i18n_metadata" text COLLATE "pg_catalog"."default",
                                             "software_id" varchar(36) COLLATE "pg_catalog"."default",
                                             "software_version" varchar(48) COLLATE "pg_catalog"."default",
                                             "id" int4 NOT NULL DEFAULT nextval('oauth2_client_id_seq'::regclass),
                                             "user_id" int4,
                                             "client_metadata" json,
                                             "issued_at" int4,
                                             "expires_at" int4
)
;

-- ----------------------------
-- Table structure for oauth2_code
-- ----------------------------
DROP TABLE IF EXISTS "oauth2_code";
CREATE TABLE "oauth2_code" (
                                           "code" varchar(120) COLLATE "pg_catalog"."default" NOT NULL,
                                           "client_id" varchar(48) COLLATE "pg_catalog"."default",
                                           "redirect_uri" text COLLATE "pg_catalog"."default",
                                           "response_type" text COLLATE "pg_catalog"."default",
                                           "scope" text COLLATE "pg_catalog"."default",
                                           "auth_time" int4 NOT NULL,
                                           "id" int4 NOT NULL DEFAULT nextval('oauth2_code_id_seq'::regclass),
                                           "user_id" int4,
                                           "code_challenge" text COLLATE "pg_catalog"."default" DEFAULT 'test'::text
)
;

-- ----------------------------
-- Table structure for oauth2_token
-- ----------------------------
DROP TABLE IF EXISTS "oauth2_token";
CREATE TABLE "oauth2_token" (
                                            "client_id" varchar(48) COLLATE "pg_catalog"."default",
                                            "token_type" varchar(40) COLLATE "pg_catalog"."default",
                                            "access_token" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
                                            "refresh_token" varchar(255) COLLATE "pg_catalog"."default",
                                            "scope" text COLLATE "pg_catalog"."default",
                                            "issued_at" int4 NOT NULL,
                                            "expires_in" int4 NOT NULL,
                                            "id" int4 NOT NULL DEFAULT nextval('oauth2_token_id_seq'::regclass),
                                            "user_id" int4,
                                            "revoked" bool
)
;

-- ----------------------------
-- Table structure for param
-- ----------------------------
DROP TABLE IF EXISTS "param";
CREATE TABLE "param" (
                                     "name" text COLLATE "pg_catalog"."default",
                                     "key" text COLLATE "pg_catalog"."default" NOT NULL,
                                     "value" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS "permission";
CREATE TABLE "permission" (
                                          "name" varchar(64) COLLATE "pg_catalog"."default",
                                          "description" varchar(255) COLLATE "pg_catalog"."default",
                                          "url" varchar(64) COLLATE "pg_catalog"."default",
                                          "method" varchar(50) COLLATE "pg_catalog"."default",
                                          "key" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
                                          "product_key" text COLLATE "pg_catalog"."default" NOT NULL
)
;
COMMENT ON COLUMN "permission"."name" IS '权限名称';
COMMENT ON COLUMN "permission"."description" IS '权限描述';
COMMENT ON COLUMN "permission"."url" IS '路由匹配地址';
COMMENT ON COLUMN "permission"."method" IS '1，get，2.post，3.put；4，delete';
COMMENT ON TABLE "permission" IS '系统权限表';

-- ----------------------------
-- Table structure for permission_scope
-- ----------------------------
DROP TABLE IF EXISTS "permission_scope";
CREATE TABLE "permission_scope" (
                                                "name" varchar(255) COLLATE "pg_catalog"."default",
                                                "key" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
                                                "parent_key" varchar(255) COLLATE "pg_catalog"."default",
                                                "product_key" text COLLATE "pg_catalog"."default" NOT NULL
)
;
COMMENT ON COLUMN "permission_scope"."key" IS '关联菜单字段';
COMMENT ON COLUMN "permission_scope"."parent_key" IS '父节点';

-- ----------------------------
-- Table structure for permission_scope_detail
-- ----------------------------
DROP TABLE IF EXISTS "permission_scope_detail";
CREATE TABLE "permission_scope_detail" (
                                                       "permission_key" varchar(255) COLLATE "pg_catalog"."default",
                                                       "permission_scope_key" varchar(255) COLLATE "pg_catalog"."default",
                                                       "id" int4 NOT NULL DEFAULT nextval('permission_scope_detail_id_seq'::regclass),
                                                       "product_key" text COLLATE "pg_catalog"."default",
                                                       "product_key_scope" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS "role";
CREATE TABLE "role" (
                                    "id" int4 NOT NULL DEFAULT nextval('role_id_seq'::regclass),
                                    "name" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
                                    "chinese_name" varchar(64) COLLATE "pg_catalog"."default",
                                    "description" varchar(255) COLLATE "pg_catalog"."default",
                                    "opr_by" varchar(32) COLLATE "pg_catalog"."default",
                                    "opr_at" int8,
                                    "del_fg" int2,
                                    "remark" text COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "role"."id" IS '角色ID';
COMMENT ON COLUMN "role"."name" IS '角色名称';
COMMENT ON COLUMN "role"."chinese_name" IS '角色中文名';
COMMENT ON COLUMN "role"."description" IS '角色描述';
COMMENT ON COLUMN "role"."opr_by" IS '操作人';
COMMENT ON COLUMN "role"."opr_at" IS '操作时间';
COMMENT ON COLUMN "role"."del_fg" IS '删除标识';
COMMENT ON TABLE "role" IS '角色表';

-- ----------------------------
-- Table structure for role_permission_scope
-- ----------------------------
DROP TABLE IF EXISTS "role_permission_scope";
CREATE TABLE "role_permission_scope" (
                                                     "role_id" int4 NOT NULL,
                                                     "permission_scope_key" varchar COLLATE "pg_catalog"."default" NOT NULL,
                                                     "id" int4 NOT NULL DEFAULT nextval('role_permission_scope_id_seq'::regclass),
                                                     "product_key" text COLLATE "pg_catalog"."default"
)
;


-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "user";
CREATE TABLE "user" (
                                    "id" int4 NOT NULL DEFAULT nextval('user_id_seq'::regclass),
                                    "name" varchar(32) COLLATE "pg_catalog"."default" NOT NULL,
                                    "telephone" varchar(16) COLLATE "pg_catalog"."default",
                                    "address" varchar(64) COLLATE "pg_catalog"."default",
                                    "loginid" varchar(255) COLLATE "pg_catalog"."default",
                                    "password" varchar(255) COLLATE "pg_catalog"."default",
                                    "token" varchar(100) COLLATE "pg_catalog"."default",
                                    "expires_in" int4,
                                    "login_at" int8,
                                    "login_ip" varchar(100) COLLATE "pg_catalog"."default",
                                    "login_count" int4 DEFAULT 0,
                                    "remark" text COLLATE "pg_catalog"."default",
                                    "opr_by" varchar(32) COLLATE "pg_catalog"."default",
                                    "opr_at" int8,
                                    "del_fg" int2,
                                    "department_key" text[] COLLATE "pg_catalog"."default",
                                    "external_id" varchar(255) COLLATE "pg_catalog"."default",
                                    "source" varchar(64) COLLATE "pg_catalog"."default",
                                    "email" varchar(255) COLLATE "pg_catalog"."default",
                                    "mobile_phone" varchar(255) COLLATE "pg_catalog"."default",
                                    "create_time" timestamp(6) DEFAULT CURRENT_TIMESTAMP,
                                    "update_time" timestamp(6),
                                    "enable" bool DEFAULT true
)
;
COMMENT ON COLUMN "user"."id" IS '用户ID';
COMMENT ON COLUMN "user"."name" IS '用户姓名';
COMMENT ON COLUMN "user"."telephone" IS '用户电话';
COMMENT ON COLUMN "user"."address" IS '用户地址';
COMMENT ON COLUMN "user"."loginid" IS '用户名';
COMMENT ON COLUMN "user"."password" IS '用户密码';
COMMENT ON COLUMN "user"."token" IS '访问凭证';
COMMENT ON COLUMN "user"."expires_in" IS '凭证有效期';
COMMENT ON COLUMN "user"."login_at" IS '登录时间';
COMMENT ON COLUMN "user"."login_ip" IS '登录IP';
COMMENT ON COLUMN "user"."login_count" IS '登录次数';
COMMENT ON COLUMN "user"."remark" IS '备注';
COMMENT ON COLUMN "user"."opr_by" IS '操作人';
COMMENT ON COLUMN "user"."opr_at" IS '操作时间';
COMMENT ON COLUMN "user"."del_fg" IS '1：已删除 0：未删除';
COMMENT ON COLUMN "user"."department_key" IS '部门编码';
COMMENT ON COLUMN "user"."external_id" IS '外部 ID';
COMMENT ON COLUMN "user"."source" IS '数据来源';
COMMENT ON COLUMN "user"."email" IS '邮件';
COMMENT ON COLUMN "user"."mobile_phone" IS '用户手机';
COMMENT ON COLUMN "user"."enable" IS '是否启用';
COMMENT ON TABLE "user" IS '用户表';

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS "user_role";
CREATE TABLE "user_role" (
                                         "id" int4 NOT NULL DEFAULT nextval('sys_user_role_id_seq'::regclass),
                                         "user_id" int4,
                                         "role_id" int4
)
;


-- ----------------------------
-- Table structure for weixin
-- ----------------------------
DROP TABLE IF EXISTS "weixin";
CREATE TABLE "weixin" (
                                      "id" int4 NOT NULL DEFAULT nextval('weixin_id_seq'::regclass),
                                      "name" varchar(32) COLLATE "pg_catalog"."default" NOT NULL,
                                      "openid" varchar(128) COLLATE "pg_catalog"."default",
                                      "createtime" timestamp(6),
                                      "updatetime" timestamp(6),
                                      "sex" varchar(8) COLLATE "pg_catalog"."default",
                                      "province" varchar(16) COLLATE "pg_catalog"."default",
                                      "city" varchar(56) COLLATE "pg_catalog"."default",
                                      "country" varchar(128) COLLATE "pg_catalog"."default",
                                      "headimgurl" varchar(16) COLLATE "pg_catalog"."default",
                                      "unionid" varchar(32) COLLATE "pg_catalog"."default" DEFAULT ''::character varying
)
;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "department_id_seq"
    OWNED BY "department"."id";


-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "oauth2_client_id_seq"
    OWNED BY "oauth2_client"."id";


-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "oauth2_code_id_seq"
    OWNED BY "oauth2_code"."id";


-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "oauth2_token_id_seq"
    OWNED BY "oauth2_token"."id";


-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "permission_scope_detail_id_seq"
    OWNED BY "permission_scope_detail"."product_key_scope";


-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "role_id_seq"
    OWNED BY "role"."id";


-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "role_permission_scope_id_seq"
    OWNED BY "role_permission_scope"."id";


-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "sys_user_role_id_seq"
    OWNED BY "user_role"."id";


-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_id_seq"
    OWNED BY "user"."id";


-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "weixin_id_seq"
    OWNED BY "weixin"."id";


-- ----------------------------
-- Indexes structure for table department
-- ----------------------------
CREATE UNIQUE INDEX "department_key_uindex" ON "department" USING btree (
                                                                                     "key" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE UNIQUE INDEX "department_name_uindex" ON "department" USING btree (
                                                                                      "name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Uniques structure for table department
-- ----------------------------
ALTER TABLE "department" ADD CONSTRAINT "department_pk_2" UNIQUE ("source", "external_id");

-- ----------------------------
-- Primary Key structure for table department
-- ----------------------------
ALTER TABLE "department" ADD CONSTRAINT "department_pk" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table license
-- ----------------------------
CREATE UNIQUE INDEX "license_product_key_uindex" ON "license" USING btree (
                                                                                       "product_key" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table license
-- ----------------------------
ALTER TABLE "license" ADD CONSTRAINT "license_pk" PRIMARY KEY ("product_key");

-- ----------------------------
-- Indexes structure for table oauth2_client
-- ----------------------------
CREATE INDEX "ix_oauth2_client_client_id" ON "oauth2_client" USING btree (
                                                                                      "client_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE INDEX "user_id" ON "oauth2_client" USING btree (
                                                                   "user_id" "pg_catalog"."int4_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table oauth2_client
-- ----------------------------
ALTER TABLE "oauth2_client" ADD CONSTRAINT "oauth2_client_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table oauth2_code
-- ----------------------------
CREATE INDEX "code" ON "oauth2_code" USING btree (
                                                              "code" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Uniques structure for table oauth2_code
-- ----------------------------
ALTER TABLE "oauth2_code" ADD CONSTRAINT "oauth2_code_code_key" UNIQUE ("code");

-- ----------------------------
-- Primary Key structure for table oauth2_code
-- ----------------------------
ALTER TABLE "oauth2_code" ADD CONSTRAINT "oauth2_code_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table oauth2_token
-- ----------------------------
CREATE INDEX "access_token" ON "oauth2_token" USING btree (
                                                                       "access_token" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE INDEX "ix_oauth2_token_refresh_token" ON "oauth2_token" USING btree (
                                                                                        "refresh_token" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE INDEX "ix_test_oauth2_token_refresh_token" ON "oauth2_token" USING btree (
                                                                                             "refresh_token" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Uniques structure for table oauth2_token
-- ----------------------------
ALTER TABLE "oauth2_token" ADD CONSTRAINT "oauth2_token_access_token_key" UNIQUE ("access_token");

-- ----------------------------
-- Primary Key structure for table oauth2_token
-- ----------------------------
ALTER TABLE "oauth2_token" ADD CONSTRAINT "oauth2_token_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table param
-- ----------------------------
CREATE UNIQUE INDEX "param_key_uindex" ON "param" USING btree (
                                                                           "key" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table param
-- ----------------------------
ALTER TABLE "param" ADD CONSTRAINT "param_pk" PRIMARY KEY ("key");

-- ----------------------------
-- Primary Key structure for table permission
-- ----------------------------
ALTER TABLE "permission" ADD CONSTRAINT "permission_pk" PRIMARY KEY ("product_key", "key");

-- ----------------------------
-- Primary Key structure for table permission_scope
-- ----------------------------
ALTER TABLE "permission_scope" ADD CONSTRAINT "permission_scope_pk" PRIMARY KEY ("product_key", "key");

-- ----------------------------
-- Indexes structure for table permission_scope_detail
-- ----------------------------
CREATE INDEX "fk_perssion_id" ON "permission_scope_detail" USING btree (
                                                                                    "permission_key" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table permission_scope_detail
-- ----------------------------
ALTER TABLE "permission_scope_detail" ADD CONSTRAINT "permission_scope_detail_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table role
-- ----------------------------
CREATE UNIQUE INDEX "role_chinese_name_uindex" ON "role" USING btree (
                                                                                  "chinese_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE UNIQUE INDEX "role_name_uindex" ON "role" USING btree (
                                                                          "name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table role
-- ----------------------------
ALTER TABLE "role" ADD CONSTRAINT "sys_role_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table role_permission_scope
-- ----------------------------
CREATE UNIQUE INDEX "role_permission_scope_id_uindex" ON "role_permission_scope" USING btree (
                                                                                                          "id" "pg_catalog"."int4_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table role_permission_scope
-- ----------------------------
ALTER TABLE "role_permission_scope" ADD CONSTRAINT "role_permission_scope_pk" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table user
-- ----------------------------
CREATE UNIQUE INDEX "username_UNIQUE" ON "user" USING btree (
                                                                         "loginid" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
COMMENT ON INDEX "username_UNIQUE" IS '用户名唯一';

-- ----------------------------
-- Uniques structure for table user
-- ----------------------------
ALTER TABLE "user" ADD CONSTRAINT "external_pk" UNIQUE ("source", "external_id");

-- ----------------------------
-- Primary Key structure for table user
-- ----------------------------
ALTER TABLE "user" ADD CONSTRAINT "sys_user_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table user_role
-- ----------------------------
ALTER TABLE "user_role" ADD CONSTRAINT "user_role_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table weixin
-- ----------------------------
ALTER TABLE "weixin" ADD CONSTRAINT "weixin_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table oauth2_client
-- ----------------------------
ALTER TABLE "oauth2_client" ADD CONSTRAINT "oauth2_client_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE SET NULL ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table oauth2_code
-- ----------------------------
ALTER TABLE "oauth2_code" ADD CONSTRAINT "oauth2_code_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- ----------------------------
-- Foreign Keys structure for table oauth2_token
-- ----------------------------
ALTER TABLE "oauth2_token" ADD CONSTRAINT "oauth2_token_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- ----------------------------
-- Foreign Keys structure for table permission_scope_detail
-- ----------------------------
ALTER TABLE "permission_scope_detail" ADD CONSTRAINT "permission_scope_detail_permission_key_product_key_fk" FOREIGN KEY ("permission_key", "product_key") REFERENCES "permission" ("key", "product_key") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "permission_scope_detail" ADD CONSTRAINT "permission_scope_detail_permission_scope_key_product_key_fk" FOREIGN KEY ("permission_scope_key", "product_key_scope") REFERENCES "permission_scope" ("key", "product_key") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table role_permission_scope
-- ----------------------------
ALTER TABLE "role_permission_scope" ADD CONSTRAINT "role_permission_scope_permission_scope_product_key_key_fk" FOREIGN KEY ("permission_scope_key", "product_key") REFERENCES "permission_scope" ("key", "product_key") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "role_permission_scope" ADD CONSTRAINT "role_permission_scope_role_id_fk" FOREIGN KEY ("role_id") REFERENCES "role" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- ----------------------------
-- Foreign Keys structure for table user_role
-- ----------------------------
ALTER TABLE "user_role" ADD CONSTRAINT "sys_user_role_role_id_fk" FOREIGN KEY ("role_id") REFERENCES "role" ("id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "user_role" ADD CONSTRAINT "user_role_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

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
DROP SEQUENCE IF EXISTS "user_auth"."department_id_seq";
CREATE SEQUENCE "user_auth"."department_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;
ALTER SEQUENCE "user_auth"."department_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for oauth2_client_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_auth"."oauth2_client_id_seq";
CREATE SEQUENCE "user_auth"."oauth2_client_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;
ALTER SEQUENCE "user_auth"."oauth2_client_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for oauth2_code_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_auth"."oauth2_code_id_seq";
CREATE SEQUENCE "user_auth"."oauth2_code_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;
ALTER SEQUENCE "user_auth"."oauth2_code_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for oauth2_token_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_auth"."oauth2_token_id_seq";
CREATE SEQUENCE "user_auth"."oauth2_token_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;
ALTER SEQUENCE "user_auth"."oauth2_token_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for permission_scope_detail_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_auth"."permission_scope_detail_id_seq";
CREATE SEQUENCE "user_auth"."permission_scope_detail_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;
ALTER SEQUENCE "user_auth"."permission_scope_detail_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for role_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_auth"."role_id_seq";
CREATE SEQUENCE "user_auth"."role_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;
ALTER SEQUENCE "user_auth"."role_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for role_permission_scope_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_auth"."role_permission_scope_id_seq";
CREATE SEQUENCE "user_auth"."role_permission_scope_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1000
    CACHE 1;
ALTER SEQUENCE "user_auth"."role_permission_scope_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for sys_user_role_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_auth"."sys_user_role_id_seq";
CREATE SEQUENCE "user_auth"."sys_user_role_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 2147483647
    START 1
    CACHE 1;
ALTER SEQUENCE "user_auth"."sys_user_role_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for user_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_auth"."user_id_seq";
CREATE SEQUENCE "user_auth"."user_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1;
ALTER SEQUENCE "user_auth"."user_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Sequence structure for weixin_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "user_auth"."weixin_id_seq";
CREATE SEQUENCE "user_auth"."weixin_id_seq"
    INCREMENT 1
    MINVALUE  1
    MAXVALUE 2147483647
    START 1
    CACHE 1;
ALTER SEQUENCE "user_auth"."weixin_id_seq" OWNER TO "postgres";

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."department";
CREATE TABLE "user_auth"."department" (
                                          "id" int4 NOT NULL DEFAULT nextval('"user_auth".department_id_seq'::regclass),
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
ALTER TABLE "user_auth"."department" OWNER TO "postgres";
COMMENT ON COLUMN "user_auth"."department"."key" IS '编码';
COMMENT ON COLUMN "user_auth"."department"."external_id" IS '外部 ID';
COMMENT ON COLUMN "user_auth"."department"."source" IS '来源';
COMMENT ON COLUMN "user_auth"."department"."order_no" IS '排序号';
COMMENT ON TABLE "user_auth"."department" IS '部门表';

-- ----------------------------
-- Table structure for license
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."license";
CREATE TABLE "user_auth"."license" (
                                       "product_key" text COLLATE "pg_catalog"."default" NOT NULL,
                                       "content" text COLLATE "pg_catalog"."default" NOT NULL
)
;
ALTER TABLE "user_auth"."license" OWNER TO "postgres";
COMMENT ON COLUMN "user_auth"."license"."product_key" IS '项目KEY';
COMMENT ON COLUMN "user_auth"."license"."content" IS '证书内容';

-- ----------------------------
-- Table structure for oauth2_client
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."oauth2_client";
CREATE TABLE "user_auth"."oauth2_client" (
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
                                             "id" int4 NOT NULL DEFAULT nextval('"user_auth".oauth2_client_id_seq'::regclass),
                                             "user_id" int4,
                                             "client_metadata" json,
                                             "issued_at" int4,
                                             "expires_at" int4
)
;
ALTER TABLE "user_auth"."oauth2_client" OWNER TO "postgres";

-- ----------------------------
-- Table structure for oauth2_code
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."oauth2_code";
CREATE TABLE "user_auth"."oauth2_code" (
                                           "code" varchar(120) COLLATE "pg_catalog"."default" NOT NULL,
                                           "client_id" varchar(48) COLLATE "pg_catalog"."default",
                                           "redirect_uri" text COLLATE "pg_catalog"."default",
                                           "response_type" text COLLATE "pg_catalog"."default",
                                           "scope" text COLLATE "pg_catalog"."default",
                                           "auth_time" int4 NOT NULL,
                                           "id" int4 NOT NULL DEFAULT nextval('"user_auth".oauth2_code_id_seq'::regclass),
                                           "user_id" int4,
                                           "code_challenge" text COLLATE "pg_catalog"."default" DEFAULT 'test'::text
)
;
ALTER TABLE "user_auth"."oauth2_code" OWNER TO "postgres";

-- ----------------------------
-- Table structure for oauth2_token
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."oauth2_token";
CREATE TABLE "user_auth"."oauth2_token" (
                                            "client_id" varchar(48) COLLATE "pg_catalog"."default",
                                            "token_type" varchar(40) COLLATE "pg_catalog"."default",
                                            "access_token" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
                                            "refresh_token" varchar(255) COLLATE "pg_catalog"."default",
                                            "scope" text COLLATE "pg_catalog"."default",
                                            "issued_at" int4 NOT NULL,
                                            "expires_in" int4 NOT NULL,
                                            "id" int4 NOT NULL DEFAULT nextval('"user_auth".oauth2_token_id_seq'::regclass),
                                            "user_id" int4,
                                            "revoked" bool
)
;
ALTER TABLE "user_auth"."oauth2_token" OWNER TO "postgres";

-- ----------------------------
-- Table structure for param
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."param";
CREATE TABLE "user_auth"."param" (
                                     "name" text COLLATE "pg_catalog"."default",
                                     "key" text COLLATE "pg_catalog"."default" NOT NULL,
                                     "value" text COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "user_auth"."param" OWNER TO "postgres";

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."permission";
CREATE TABLE "user_auth"."permission" (
                                          "name" varchar(64) COLLATE "pg_catalog"."default",
                                          "description" varchar(255) COLLATE "pg_catalog"."default",
                                          "url" varchar(64) COLLATE "pg_catalog"."default",
                                          "method" varchar(50) COLLATE "pg_catalog"."default",
                                          "key" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
                                          "product_key" text COLLATE "pg_catalog"."default" NOT NULL
)
;
ALTER TABLE "user_auth"."permission" OWNER TO "postgres";
COMMENT ON COLUMN "user_auth"."permission"."name" IS '权限名称';
COMMENT ON COLUMN "user_auth"."permission"."description" IS '权限描述';
COMMENT ON COLUMN "user_auth"."permission"."url" IS '路由匹配地址';
COMMENT ON COLUMN "user_auth"."permission"."method" IS '1，get，2.post，3.put；4，delete';
COMMENT ON TABLE "user_auth"."permission" IS '系统权限表';

-- ----------------------------
-- Table structure for permission_scope
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."permission_scope";
CREATE TABLE "user_auth"."permission_scope" (
                                                "name" varchar(255) COLLATE "pg_catalog"."default",
                                                "key" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
                                                "parent_key" varchar(255) COLLATE "pg_catalog"."default",
                                                "product_key" text COLLATE "pg_catalog"."default" NOT NULL
)
;
ALTER TABLE "user_auth"."permission_scope" OWNER TO "postgres";
COMMENT ON COLUMN "user_auth"."permission_scope"."key" IS '关联菜单字段';
COMMENT ON COLUMN "user_auth"."permission_scope"."parent_key" IS '父节点';

-- ----------------------------
-- Table structure for permission_scope_detail
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."permission_scope_detail";
CREATE TABLE "user_auth"."permission_scope_detail" (
                                                       "permission_key" varchar(255) COLLATE "pg_catalog"."default",
                                                       "permission_scope_key" varchar(255) COLLATE "pg_catalog"."default",
                                                       "id" int4 NOT NULL DEFAULT nextval('"user_auth".permission_scope_detail_id_seq'::regclass),
                                                       "product_key" text COLLATE "pg_catalog"."default",
                                                       "product_key_scope" text COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "user_auth"."permission_scope_detail" OWNER TO "postgres";

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."role";
CREATE TABLE "user_auth"."role" (
                                    "id" int4 NOT NULL DEFAULT nextval('"user_auth".role_id_seq'::regclass),
                                    "name" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
                                    "chinese_name" varchar(64) COLLATE "pg_catalog"."default",
                                    "description" varchar(255) COLLATE "pg_catalog"."default",
                                    "opr_by" varchar(32) COLLATE "pg_catalog"."default",
                                    "opr_at" int8,
                                    "del_fg" int2,
                                    "remark" text COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "user_auth"."role" OWNER TO "postgres";
COMMENT ON COLUMN "user_auth"."role"."id" IS '角色ID';
COMMENT ON COLUMN "user_auth"."role"."name" IS '角色名称';
COMMENT ON COLUMN "user_auth"."role"."chinese_name" IS '角色中文名';
COMMENT ON COLUMN "user_auth"."role"."description" IS '角色描述';
COMMENT ON COLUMN "user_auth"."role"."opr_by" IS '操作人';
COMMENT ON COLUMN "user_auth"."role"."opr_at" IS '操作时间';
COMMENT ON COLUMN "user_auth"."role"."del_fg" IS '删除标识';
COMMENT ON TABLE "user_auth"."role" IS '角色表';

-- ----------------------------
-- Table structure for role_permission_scope
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."role_permission_scope";
CREATE TABLE "user_auth"."role_permission_scope" (
                                                     "role_id" int4 NOT NULL,
                                                     "permission_scope_key" varchar COLLATE "pg_catalog"."default" NOT NULL,
                                                     "id" int4 NOT NULL DEFAULT nextval('"user_auth".role_permission_scope_id_seq'::regclass),
                                                     "product_key" text COLLATE "pg_catalog"."default"
)
;
ALTER TABLE "user_auth"."role_permission_scope" OWNER TO "postgres";
COMMENT ON TABLE "user_auth"."role_permission_scope" IS '权限角色表
';

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."user";
CREATE TABLE "user_auth"."user" (
                                    "id" int4 NOT NULL DEFAULT nextval('"user_auth".user_id_seq'::regclass),
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
ALTER TABLE "user_auth"."user" OWNER TO "postgres";
COMMENT ON COLUMN "user_auth"."user"."id" IS '用户ID';
COMMENT ON COLUMN "user_auth"."user"."name" IS '用户姓名';
COMMENT ON COLUMN "user_auth"."user"."telephone" IS '用户电话';
COMMENT ON COLUMN "user_auth"."user"."address" IS '用户地址';
COMMENT ON COLUMN "user_auth"."user"."loginid" IS '用户名';
COMMENT ON COLUMN "user_auth"."user"."password" IS '用户密码';
COMMENT ON COLUMN "user_auth"."user"."token" IS '访问凭证';
COMMENT ON COLUMN "user_auth"."user"."expires_in" IS '凭证有效期';
COMMENT ON COLUMN "user_auth"."user"."login_at" IS '登录时间';
COMMENT ON COLUMN "user_auth"."user"."login_ip" IS '登录IP';
COMMENT ON COLUMN "user_auth"."user"."login_count" IS '登录次数';
COMMENT ON COLUMN "user_auth"."user"."remark" IS '备注';
COMMENT ON COLUMN "user_auth"."user"."opr_by" IS '操作人';
COMMENT ON COLUMN "user_auth"."user"."opr_at" IS '操作时间';
COMMENT ON COLUMN "user_auth"."user"."del_fg" IS '1：已删除 0：未删除';
COMMENT ON COLUMN "user_auth"."user"."department_key" IS '部门编码';
COMMENT ON COLUMN "user_auth"."user"."external_id" IS '外部 ID';
COMMENT ON COLUMN "user_auth"."user"."source" IS '数据来源';
COMMENT ON COLUMN "user_auth"."user"."email" IS '邮件';
COMMENT ON COLUMN "user_auth"."user"."mobile_phone" IS '用户手机';
COMMENT ON COLUMN "user_auth"."user"."enable" IS '是否启用';
COMMENT ON TABLE "user_auth"."user" IS '用户表';

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."user_role";
CREATE TABLE "user_auth"."user_role" (
                                         "id" int4 NOT NULL DEFAULT nextval('"user_auth".sys_user_role_id_seq'::regclass),
                                         "user_id" int4,
                                         "role_id" int4
)
;
ALTER TABLE "user_auth"."user_role" OWNER TO "postgres";
COMMENT ON TABLE "user_auth"."user_role" IS '用户角色表';

-- ----------------------------
-- Table structure for weixin
-- ----------------------------
DROP TABLE IF EXISTS "user_auth"."weixin";
CREATE TABLE "user_auth"."weixin" (
                                      "id" int4 NOT NULL DEFAULT nextval('"user_auth".weixin_id_seq'::regclass),
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
ALTER TABLE "user_auth"."weixin" OWNER TO "postgres";

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."department_id_seq"
    OWNED BY "user_auth"."department"."id";
SELECT setval('"user_auth"."department_id_seq"', 600, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."oauth2_client_id_seq"
    OWNED BY "user_auth"."oauth2_client"."id";
SELECT setval('"user_auth"."oauth2_client_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."oauth2_code_id_seq"
    OWNED BY "user_auth"."oauth2_code"."id";
SELECT setval('"user_auth"."oauth2_code_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."oauth2_token_id_seq"
    OWNED BY "user_auth"."oauth2_token"."id";
SELECT setval('"user_auth"."oauth2_token_id_seq"', 2238, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."permission_scope_detail_id_seq"
    OWNED BY "user_auth"."permission_scope_detail"."product_key_scope";
SELECT setval('"user_auth"."permission_scope_detail_id_seq"', 788, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."role_id_seq"
    OWNED BY "user_auth"."role"."id";
SELECT setval('"user_auth"."role_id_seq"', 29, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."role_permission_scope_id_seq"
    OWNED BY "user_auth"."role_permission_scope"."id";
SELECT setval('"user_auth"."role_permission_scope_id_seq"', 1372, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."sys_user_role_id_seq"
    OWNED BY "user_auth"."user_role"."id";
SELECT setval('"user_auth"."sys_user_role_id_seq"', 98, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."user_id_seq"
    OWNED BY "user_auth"."user"."id";
SELECT setval('"user_auth"."user_id_seq"', 20629, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "user_auth"."weixin_id_seq"
    OWNED BY "user_auth"."weixin"."id";
SELECT setval('"user_auth"."weixin_id_seq"', 2, false);

-- ----------------------------
-- Indexes structure for table department
-- ----------------------------
CREATE UNIQUE INDEX "department_key_uindex" ON "user_auth"."department" USING btree (
                                                                                     "key" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE UNIQUE INDEX "department_name_uindex" ON "user_auth"."department" USING btree (
                                                                                      "name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Uniques structure for table department
-- ----------------------------
ALTER TABLE "user_auth"."department" ADD CONSTRAINT "department_pk_2" UNIQUE ("source", "external_id");

-- ----------------------------
-- Primary Key structure for table department
-- ----------------------------
ALTER TABLE "user_auth"."department" ADD CONSTRAINT "department_pk" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table license
-- ----------------------------
CREATE UNIQUE INDEX "license_product_key_uindex" ON "user_auth"."license" USING btree (
                                                                                       "product_key" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table license
-- ----------------------------
ALTER TABLE "user_auth"."license" ADD CONSTRAINT "license_pk" PRIMARY KEY ("product_key");

-- ----------------------------
-- Indexes structure for table oauth2_client
-- ----------------------------
CREATE INDEX "ix_oauth2_client_client_id" ON "user_auth"."oauth2_client" USING btree (
                                                                                      "client_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE INDEX "user_id" ON "user_auth"."oauth2_client" USING btree (
                                                                   "user_id" "pg_catalog"."int4_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table oauth2_client
-- ----------------------------
ALTER TABLE "user_auth"."oauth2_client" ADD CONSTRAINT "oauth2_client_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table oauth2_code
-- ----------------------------
CREATE INDEX "code" ON "user_auth"."oauth2_code" USING btree (
                                                              "code" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Uniques structure for table oauth2_code
-- ----------------------------
ALTER TABLE "user_auth"."oauth2_code" ADD CONSTRAINT "oauth2_code_code_key" UNIQUE ("code");

-- ----------------------------
-- Primary Key structure for table oauth2_code
-- ----------------------------
ALTER TABLE "user_auth"."oauth2_code" ADD CONSTRAINT "oauth2_code_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table oauth2_token
-- ----------------------------
CREATE INDEX "access_token" ON "user_auth"."oauth2_token" USING btree (
                                                                       "access_token" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE INDEX "ix_oauth2_token_refresh_token" ON "user_auth"."oauth2_token" USING btree (
                                                                                        "refresh_token" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE INDEX "ix_test_oauth2_token_refresh_token" ON "user_auth"."oauth2_token" USING btree (
                                                                                             "refresh_token" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Uniques structure for table oauth2_token
-- ----------------------------
ALTER TABLE "user_auth"."oauth2_token" ADD CONSTRAINT "oauth2_token_access_token_key" UNIQUE ("access_token");

-- ----------------------------
-- Primary Key structure for table oauth2_token
-- ----------------------------
ALTER TABLE "user_auth"."oauth2_token" ADD CONSTRAINT "oauth2_token_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table param
-- ----------------------------
CREATE UNIQUE INDEX "param_key_uindex" ON "user_auth"."param" USING btree (
                                                                           "key" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table param
-- ----------------------------
ALTER TABLE "user_auth"."param" ADD CONSTRAINT "param_pk" PRIMARY KEY ("key");

-- ----------------------------
-- Primary Key structure for table permission
-- ----------------------------
ALTER TABLE "user_auth"."permission" ADD CONSTRAINT "permission_pk" PRIMARY KEY ("product_key", "key");

-- ----------------------------
-- Primary Key structure for table permission_scope
-- ----------------------------
ALTER TABLE "user_auth"."permission_scope" ADD CONSTRAINT "permission_scope_pk" PRIMARY KEY ("product_key", "key");

-- ----------------------------
-- Indexes structure for table permission_scope_detail
-- ----------------------------
CREATE INDEX "fk_perssion_id" ON "user_auth"."permission_scope_detail" USING btree (
                                                                                    "permission_key" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table permission_scope_detail
-- ----------------------------
ALTER TABLE "user_auth"."permission_scope_detail" ADD CONSTRAINT "permission_scope_detail_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table role
-- ----------------------------
CREATE UNIQUE INDEX "role_chinese_name_uindex" ON "user_auth"."role" USING btree (
                                                                                  "chinese_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
CREATE UNIQUE INDEX "role_name_uindex" ON "user_auth"."role" USING btree (
                                                                          "name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table role
-- ----------------------------
ALTER TABLE "user_auth"."role" ADD CONSTRAINT "sys_role_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table role_permission_scope
-- ----------------------------
CREATE UNIQUE INDEX "role_permission_scope_id_uindex" ON "user_auth"."role_permission_scope" USING btree (
                                                                                                          "id" "pg_catalog"."int4_ops" ASC NULLS LAST
    );

-- ----------------------------
-- Primary Key structure for table role_permission_scope
-- ----------------------------
ALTER TABLE "user_auth"."role_permission_scope" ADD CONSTRAINT "role_permission_scope_pk" PRIMARY KEY ("id");

-- ----------------------------
-- Indexes structure for table user
-- ----------------------------
CREATE UNIQUE INDEX "username_UNIQUE" ON "user_auth"."user" USING btree (
                                                                         "loginid" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
    );
COMMENT ON INDEX "user_auth"."username_UNIQUE" IS '用户名唯一';

-- ----------------------------
-- Uniques structure for table user
-- ----------------------------
ALTER TABLE "user_auth"."user" ADD CONSTRAINT "external_pk" UNIQUE ("source", "external_id");

-- ----------------------------
-- Primary Key structure for table user
-- ----------------------------
ALTER TABLE "user_auth"."user" ADD CONSTRAINT "sys_user_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table user_role
-- ----------------------------
ALTER TABLE "user_auth"."user_role" ADD CONSTRAINT "user_role_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table weixin
-- ----------------------------
ALTER TABLE "user_auth"."weixin" ADD CONSTRAINT "weixin_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table oauth2_client
-- ----------------------------
ALTER TABLE "user_auth"."oauth2_client" ADD CONSTRAINT "oauth2_client_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "user_auth"."user" ("id") ON DELETE SET NULL ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table oauth2_code
-- ----------------------------
ALTER TABLE "user_auth"."oauth2_code" ADD CONSTRAINT "oauth2_code_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "user_auth"."user" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- ----------------------------
-- Foreign Keys structure for table oauth2_token
-- ----------------------------
ALTER TABLE "user_auth"."oauth2_token" ADD CONSTRAINT "oauth2_token_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "user_auth"."user" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- ----------------------------
-- Foreign Keys structure for table permission_scope_detail
-- ----------------------------
ALTER TABLE "user_auth"."permission_scope_detail" ADD CONSTRAINT "permission_scope_detail_permission_key_product_key_fk" FOREIGN KEY ("permission_key", "product_key") REFERENCES "user_auth"."permission" ("key", "product_key") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "user_auth"."permission_scope_detail" ADD CONSTRAINT "permission_scope_detail_permission_scope_key_product_key_fk" FOREIGN KEY ("permission_scope_key", "product_key_scope") REFERENCES "user_auth"."permission_scope" ("key", "product_key") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table role_permission_scope
-- ----------------------------
ALTER TABLE "user_auth"."role_permission_scope" ADD CONSTRAINT "role_permission_scope_permission_scope_product_key_key_fk" FOREIGN KEY ("permission_scope_key", "product_key") REFERENCES "user_auth"."permission_scope" ("key", "product_key") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "user_auth"."role_permission_scope" ADD CONSTRAINT "role_permission_scope_role_id_fk" FOREIGN KEY ("role_id") REFERENCES "user_auth"."role" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- ----------------------------
-- Foreign Keys structure for table user_role
-- ----------------------------
ALTER TABLE "user_auth"."user_role" ADD CONSTRAINT "sys_user_role_role_id_fk" FOREIGN KEY ("role_id") REFERENCES "user_auth"."role" ("id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "user_auth"."user_role" ADD CONSTRAINT "user_role_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "user_auth"."user" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

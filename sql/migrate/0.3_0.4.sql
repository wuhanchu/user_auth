COMMENT ON TABLE "user_auth"."role_permission_scope" IS '权限角色表
';

ALTER TABLE "user_auth"."user" ALTER COLUMN "name" SET NOT NULL;

ALTER TABLE "user_auth"."user" ALTER COLUMN "loginid" DROP NOT NULL;

ALTER TABLE "user_auth"."user" ALTER COLUMN "password" DROP NOT NULL;

ALTER TABLE "user_auth"."user" ADD COLUMN "external_id" json;

COMMENT ON COLUMN "user_auth"."user"."external_id" IS '外部 ID';

ALTER TABLE "user_auth"."user" ADD COLUMN "source" varchar(64) COLLATE "pg_catalog"."default";

COMMENT ON COLUMN "user_auth"."user"."source" IS '数据来源';

ALTER TABLE "user_auth"."user" ADD COLUMN "email" varchar(255) COLLATE "pg_catalog"."default";

COMMENT ON COLUMN "user_auth"."user"."email" IS '邮件';

ALTER TABLE "user_auth"."user" ADD COLUMN "mobile_phone" varchar(255) COLLATE "pg_catalog"."default";

COMMENT ON COLUMN "user_auth"."user"."mobile_phone" IS '用户手机';

ALTER TABLE "user_auth"."user_role" DROP CONSTRAINT "sys_user_role_user_id_fk";

UPDATE "param" SET name = '版本', value = '0.4' WHERE key = 'version';


CREATE SEQUENCE "user_auth"."config_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

CREATE TABLE "user_auth"."config" (
  "key" text COLLATE "pg_catalog"."default" NOT NULL,
  "name" text COLLATE "pg_catalog"."default",
  "value" text COLLATE "pg_catalog"."default",
  "remark" text COLLATE "pg_catalog"."default",
  "id" int4 NOT NULL DEFAULT nextval('"user_auth".config_id_seq'::regclass),
  CONSTRAINT "config_pkey" PRIMARY KEY ("id")
)
;

COMMENT ON COLUMN "user_auth"."config"."key" IS '名称';

COMMENT ON COLUMN "user_auth"."config"."remark" IS '备注';

COMMENT ON TABLE "user_auth"."config" IS '配置';

ALTER SEQUENCE "user_auth"."config_id_seq"
OWNED BY "user_auth"."config"."id";

UPDATE
    "param"
SET
    value = '0.12.1'
WHERE
    key = 'version';
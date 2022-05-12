ALTER TABLE "department"
    ADD COLUMN "create_time" timestamp(6) DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE "department"
    ADD COLUMN "update_time" timestamp(6);

ALTER TABLE "department"
    ADD COLUMN "external_id" varchar(256) COLLATE "pg_catalog"."default";

COMMENT ON COLUMN "department"."external_id" IS '外部 ID';

ALTER TABLE "department"
    ADD COLUMN "source" varchar(64) COLLATE "pg_catalog"."default";

COMMENT ON COLUMN "department"."source" IS '来源';

ALTER TABLE "department"
    ADD COLUMN "remark" text COLLATE "pg_catalog"."default";

ALTER TABLE "department"
    ADD CONSTRAINT "department_pk" PRIMARY KEY ("id");

ALTER TABLE "department"
    ADD CONSTRAINT "department_pk_2" UNIQUE ("source", "external_id");

ALTER TABLE "role"
    ADD COLUMN "remark" text COLLATE "pg_catalog"."default";

ALTER TABLE "user"
    ALTER COLUMN "remark" TYPE text COLLATE "pg_catalog"."default" USING "remark"::text;

ALTER TABLE "user"
    ALTER COLUMN "external_id" TYPE varchar(255) COLLATE "pg_catalog"."default" USING "external_id"::varchar(255);

ALTER TABLE "user"
    ADD COLUMN "create_time" timestamp(6) DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE "user"
    ADD COLUMN "update_time" timestamp(6);

ALTER TABLE "user"
    ADD CONSTRAINT "external_pk" UNIQUE ("source", "external_id");

UPDATE "param" SET name = '版本', value = '0.5' WHERE key = 'version';

ALTER TABLE "user_auth"."department"
    ADD COLUMN "order_no" int4;

COMMENT ON COLUMN "user_auth"."department"."order_no" IS '排序号';

ALTER TABLE "user_auth"."user"
    ADD COLUMN "enable" bool DEFAULT true;

COMMENT ON COLUMN "user_auth"."user"."enable" IS '是否启用';

ALTER TABLE "user_auth"."user"
    DROP COLUMN "enabled" CASCADE;

drop view IF EXISTS  "user_auth"."user_extend" cascade ;

CREATE VIEW "user_auth"."user_extend" AS
SELECT "user".id,
       "user".name,
       "user".telephone,
       "user".address,
       "user".loginid,
       "user".password,
       "user".token,
       "user".expires_in,
       "user".login_at,
       "user".login_ip,
       "user".login_count,
       "user".remark,
       "user".opr_by,
       "user".opr_at,
       "user".del_fg,
       "user".department_key,
       "user".external_id,
       "user".source,
       "user".email,
       "user".mobile_phone,
       "user".create_time,
       "user".update_time,
       "user".enable,
       array_agg(ur.role_id) FILTER (WHERE ur.role_id IS NOT NULL) AS roles
FROM user_auth."user"
         LEFT JOIN user_auth.user_role ur ON "user".id = ur.user_id
GROUP BY "user".id;

ALTER TABLE "user_auth"."user_extend"
    OWNER TO "postgres";

UPDATE "user_auth"."param"
SET name  = '版本',
    value = '0.7'
WHERE key = 'version';

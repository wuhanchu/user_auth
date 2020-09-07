ALTER TABLE "role_permission_scope"
    DROP CONSTRAINT "role_permission_scope_permission_scope_product_key_key_fk";

ALTER TABLE "role_permission_scope"
    ADD CONSTRAINT "role_permission_scope_permission_scope_product_key_key_fk" FOREIGN KEY ("product_key", "permission_scope_key") REFERENCES "permission_scope" ("key", "product_key") ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "user_role"
    ADD CONSTRAINT "user_role_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE "department"
    ALTER COLUMN "id" SET DEFAULT nextval('department_id_seq'::regclass);

ALTER TABLE "role_permission_scope"
    ADD CONSTRAINT "role_permission_scope_permission_scope_product_key_key_fk" FOREIGN KEY ("product_key", "permission_scope_key") REFERENCES "permission_scope" ("key", "product_key") ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "user_role"
    ADD CONSTRAINT "user_role_user_id_fk" FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

UPDATE "param" SET name = '版本', value = '0.6' WHERE key = 'version';

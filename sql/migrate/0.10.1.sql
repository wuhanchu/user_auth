ALTER TABLE "role_permission_scope" drop CONSTRAINT if exists "role_permission_scope_permission_scope_product_key_key_fk" ;

UPDATE
    "param"
SET
    value = '0.10.1'
WHERE
    key = 'version';
CREATE SEQUENCE "user_auth"."config_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

ALTER SEQUENCE "user_auth"."config_id_seq"
OWNED BY "user_auth"."config"."id";

UPDATE
    "param"
SET
    value = '0.10.1'
WHERE
    key = 'version';
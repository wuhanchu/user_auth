INSERT INTO "oauth2_client"("client_id", "client_secret", "client_id_issued_at", "client_secret_expires_at",
                            "redirect_uri", "token_endpoint_auth_method", "grant_type", "response_type", "scope",
                            "client_name", "client_uri", "logo_uri", "contact", "tos_uri", "policy_uri", "jwks_uri",
                            "jwks_text", "i18n_metadata", "software_id", "software_version", "user_id",
                            "client_metadata", "issued_at", "expires_at")
VALUES ('yAl9PO9sA4NKYhcrXfAOXxlD', 'DarmrCkeA04rV8t8vA4mTXhMvn7nEUweE07JgvWhEVpGsukK', 1565360863, 0,
        'http://localhost:5002/api/v1/users?limit=10&offset=0', 'client_secret_basic', 'authorization_code
password', 'code', 'profile', 'system', 'http://localhost:5002', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
        NULL, 1, '{"grant_types": ["authorization_code","password","client_credentials"], "response_types":"code", "scope":"profile"}', NULL,
        NULL);

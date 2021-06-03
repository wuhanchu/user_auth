INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/authorize', 'GET', 'auth_authorize_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/authorize', 'POST', 'auth_authorize_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/create_client', 'GET', 'auth_create_client_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/create_client', 'POST', 'auth_create_client_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/', 'GET', 'auth_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_登出', NULL, '/auth/logout', 'GET', 'auth_logout_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/', 'POST', 'auth_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/revoke', 'POST', 'auth_revoke_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_登录', NULL, '/auth/token', 'POST', 'auth_token_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('证书_校验', NULL, '/license/check', 'GET', 'license_check_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('证书_构造', NULL, '/license/file', 'POST', 'license_file_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('证书_查询', NULL, '/license', 'GET', 'license_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('证书_上传', NULL, '/license', 'POST', 'license_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('客户端_删除', NULL, '/oauth2_client', 'DELETE', 'oauth2_client_delete', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('客户端_查询', NULL, '/oauth2_client', 'GET', 'oauth2_client_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('客户端_修改', NULL, '/oauth2_client', 'PATCH', 'oauth2_client_patch', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('客户端_新增', NULL, '/oauth2_client', 'POST', 'oauth2_client_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('客户端_覆盖', NULL, '/oauth2_client', 'PUT', 'oauth2_client_put', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('接口_删除', NULL, '/permission', 'DELETE', 'permission_delete', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('接口_查询', NULL, '/permission', 'GET', 'permission_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('接口_修改', NULL, '/permission', 'PATCH', 'permission_patch', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('接口_新增', NULL, '/permission', 'POST', 'permission_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('接口_覆盖', NULL, '/permission', 'PUT', 'permission_put', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('功能_删除', NULL, '/permission_scope', 'DELETE', 'permission_scope_delete', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('功能_查询', NULL, '/permission_scope', 'GET', 'permission_scope_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('功能_修改', NULL, '/permission_scope', 'PATCH', 'permission_scope_patch', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_删除', NULL, '/project', 'DELETE', 'project_delete', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目文件_删除', NULL, '/project_item', 'DELETE', 'project_item_delete', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目文件_查询', NULL, '/project_item', 'GET', 'project_item_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目文件_新增', NULL, '/project_item', 'POST', 'project_item_post', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目文件_覆盖', NULL, '/project_item', 'PUT', 'project_item_put', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_新增', NULL, '/project', 'POST', 'project_post', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_覆盖', NULL, '/project', 'PUT', 'project_put', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目人员_删除', NULL, '/project_user', 'DELETE', 'project_user_delete', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目人员_查询', NULL, '/project_user', 'GET', 'project_user_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目人员_覆盖', NULL, '/project_user', 'PUT', 'project_user_put', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('角色_查询', NULL, '/role', 'GET', 'role_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('功能_新增', NULL, '/permission_scope', 'POST', 'permission_scope_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('功能_覆盖', NULL, '/permission_scope', 'PUT', 'permission_scope_put', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_导出', NULL, '/project/export', 'GET', 'project_export_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_查询', NULL, '/project', 'GET', 'project_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目文件_音频文件_获取', NULL, '/project_item/audio', 'GET', 'project_item_audio_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目文件_修改', NULL, '/project_item', 'PATCH', 'project_item_patch', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目文件_音频文件_上传', NULL, '/project_item/upload', 'POST', 'project_item_upload_post', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_修改', NULL, '/project', 'PATCH', 'project_patch', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目人员_修改', NULL, '/project_user', 'PATCH', 'project_user_patch', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目人员_新增', NULL, '/project_user', 'POST', 'project_user_post', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('问题_删除', NULL, '/question', 'DELETE', 'question_delete', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('问题_查询', NULL, '/question', 'GET', 'question_get', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('问题_修改', NULL, '/question', 'PATCH', 'question_patch', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('问题_新增', NULL, '/question', 'POST', 'question_post', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('问题_覆盖', NULL, '/question', 'PUT', 'question_put', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('角色_删除', NULL, '/role', 'DELETE', 'role_delete', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('角色_修改', NULL, '/role', 'PATCH', 'role_patch', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('角色_权限_查询', NULL, '/role/permission', 'GET', 'role_permission_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('角色_功能_查询', NULL, '/role/permission_scope', 'GET', 'role_permission_scope_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('角色_功能_覆盖', NULL, '/role/permission_scope', 'PUT', 'role_permission_scope_put', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('角色_新增', NULL, '/role', 'POST', 'role_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('角色_覆盖', NULL, '/role', 'PUT', 'role_put', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('服务_删除', NULL, '/service', 'DELETE', 'service_delete', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('服务_查询', NULL, '/service', 'GET', 'service_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('服务_修改', NULL, '/service', 'PATCH', 'service_patch', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('服务_新增', NULL, '/service', 'POST', 'service_post', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('服务_覆盖', NULL, '/service', 'PUT', 'service_put', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/static/<path:filename>', 'GET', 'static_<path:filename>_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('工具_文本报告', NULL, '/tool/report', 'POST', 'tool_report_post', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_当前', NULL, '/user/current', 'GET', 'user_current_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_删除', NULL, '/user', 'DELETE', 'user_delete', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_查询', NULL, '/user', 'GET', 'user_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_质检_查询', NULL, '/user/inspection', 'GET', 'user_inspection_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_标注_查询', NULL, '/user/item', 'GET', 'user_item_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_标注_下一个', NULL, '/user/item/next', 'GET', 'user_item_next_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_密码_修改', NULL, '/user/password', 'PUT', 'user_password_put', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_修改', NULL, '/user', 'PATCH', 'user_patch', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_新增', NULL, '/user', 'POST', 'user_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_项目_查询', NULL, '/user/project', 'GET', 'user_project_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_覆盖', NULL, '/user', 'PUT', 'user_put', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_角色_获取', NULL, '/user/role', 'GET', 'user_role_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('用户_角色_覆盖', NULL, '/user/role', 'PUT', 'user_role_put', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/', 'GET', 'auth__get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/', 'POST', 'auth__post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/auth/token', 'DELETE', 'auth_token_delete', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_删除', NULL, '/project', 'DELETE', 'project_delete', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_查询', NULL, '/project', 'GET', 'project_get', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_修改', NULL, '/project', 'PATCH', 'project_patch', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_新增', NULL, '/project', 'POST', 'project_post', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_覆盖', NULL, '/project', 'PUT', 'project_put', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_查询_统计', NULL, '/project_statistic', 'GET', 'project_statistic', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_用户_统计', NULL, '/project_user_statistic', 'GET', 'project_user_statistic', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/static/<path:filename>', 'GET', 'static_<path:filename>_get', 'z_know_info');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目文件_查询_视图', NULL, '/project_item_extend', 'GET', 'project_item_get_extend', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/debug-sentry', 'GET', 'debug-sentry_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/debug-sentry', 'GET', 'debug-sentry_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('部门_删除', NULL, '/department', 'DELETE', 'department_delete', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('部门_查询', NULL, '/department', 'GET', 'department_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('部门_修改', NULL, '/department', 'PATCH', 'department_patch', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('部门_新增', NULL, '/department', 'POST', 'department_post', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('部门_覆盖', NULL, '/department', 'PUT', 'department_put', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/static/<path:filename>', 'GET', 'static_<path:filename>_get', 'user_auth');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/debug-sentry', 'GET', 'debug-sentry_get', 'z_ai_service');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('文件_明细', NULL, '/project_data/details', 'GET', 'details', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('人员_淘汰', NULL, '/project_user/eliminate', 'DELETE', 'eliminate', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('更新项目文件', NULL, '/project/item', 'PATCH', 'patch', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目_进度', NULL, '/project_data', NULL, 'project_data', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/static/<path:filename>', 'GET', 'static_<path:filename>_get', 'z_ai_service');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目过滤统计', NULL, 'project/statistic', 'GET', 'project_statics', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES (NULL, NULL, '/project/font/report', 'GET', 'font_report', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('团队管理', NULL, '/team_statistic', 'GET', 'team_statistic', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('我的团队', NULL, '/user/team', 'GET', 'user_team_get', 'z_markgo');
INSERT INTO "permission"("name", "description", "url", "method", "key", "product_key") VALUES ('项目验收', NULL, '/acceptance/statistic', 'GET', 'acceptance_get', 'z_markgo');

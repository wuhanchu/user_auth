INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('证书', 'license', 'system', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('证书_校验', 'license_check_get', 'license', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('证书_构造', 'license_file_post', 'license', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('证书_上传', 'license_post', 'license', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('登录', 'login', NULL, 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_音频导出', 'project_export', 'project_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_导入', 'project_import', 'project_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_文本导出', 'project_item_export', 'project_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目文件_上传', 'project_item_upload_post', 'project_item_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_修改', 'project_patch', 'project_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('问题_删除', 'question_delete', 'question_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('问题_导出', 'question_export', 'question_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('问题_导入', 'question_import', 'question_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('问题_修改', 'question_patch', 'question_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('问题_新增', 'question_post', 'question_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('角色_删除', 'role_delete', 'role_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('角色', 'role_get', 'system', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('角色_修改', 'role_patch', 'role_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('角色_权限', 'role_permission_get', 'role_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('角色_功能', 'role_permission_scope_get', 'role_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('角色_功能_覆盖', 'role_permission_scope_put', 'role_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('角色_新增', 'role_post', 'role_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('文本报告', 'tool_report_post', 'tool', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('用户_删除', 'user_delete', 'user_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('用户', 'user_get', 'system', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('去质检', 'user_inspection_next_get', 'user_inspection_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('去标注', 'user_item_next_get', 'user_item_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('用户_修改', 'user_patch', 'user_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('用户_新增', 'user_post', 'user_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('分配角色', 'user_role_put', 'user_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_删除', 'project_delete', 'project_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目文件_删除', 'project_item_delete', 'project_item_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目文件', 'project_item_get', 'project_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_新增', 'project_post', 'project_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目人员', 'project_user_get', 'project_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目人员_分配', 'project_user_put', 'project_user_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('系统管理', 'system', 'login', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_删除', 'project_delete', 'project_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_导出', 'project_export', 'project_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_修改', 'project_patch', 'project_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目_新增', 'project_post', 'project_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('服务_删除', 'service_delete', 'service_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('AI服务', 'service_get', 'system', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('服务_修改', 'service_patch', 'service_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('服务_新增', 'service_post', 'service_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('问题_覆盖', 'question_put', 'question_get', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('知料', 'z_know_info', 'login', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('标注狗', 'z_markgo', 'login', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目', 'project_get', 'z_know_info', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('我的项目', 'project_get', 'z_markgo', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('问题', 'question_get', 'z_know_info', 'z_know_info');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('工具', 'tool', 'z_markgo', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('我的质检', 'user_inspection_get', 'z_markgo', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('我的标注', 'user_item_get', 'z_markgo', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目文件_重分配', 'project_item_put', 'project_item_get', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('部门_删除', 'department_delete', 'department_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('部门_导出', 'department_export', 'department_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('部门', 'department_get', 'login', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('部门_导入', 'department_import', 'department_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('部门_修改', 'department_patch', 'department_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('部门_新增', 'department_post', 'department_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('客户端_删除', 'oauth2_client_delete', 'oauth2_client_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('客户端_导出', 'oauth2_client_export', 'oauth2_client_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('客户端', 'oauth2_client_get', 'login', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('客户端_导入', 'oauth2_client_import', 'oauth2_client_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('客户端_修改', 'oauth2_client_patch', 'oauth2_client_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('客户端_新增', 'oauth2_client_post', 'oauth2_client_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('接口_删除', 'permission_delete', 'permission_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('接口_导出', 'permission_export', 'permission_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('接口', 'permission_get', 'login', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('接口_导入', 'permission_import', 'permission_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('接口_修改', 'permission_patch', 'permission_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('接口_新增', 'permission_post', 'permission_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('功能_删除', 'permission_scope_delete', 'permission_scope_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('功能_导出', 'permission_scope_export', 'permission_scope_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('功能', 'permission_scope_get', 'login', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('功能_导入', 'permission_scope_import', 'permission_scope_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('功能_修改', 'permission_scope_patch', 'permission_scope_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('功能_新增', 'permission_scope_post', 'permission_scope_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('角色_导出', 'role_export', 'role_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('角色_导入', 'role_import', 'role_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('用户_导出', 'user_export', 'user_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('用户_导入', 'user_import', 'user_get', 'user_auth');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('团队管理', 'team_get', 'z_markgo', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('我的团队', 'user_team_get', 'z_markgo', 'z_markgo');
INSERT INTO "permission_scope"("name", "key", "parent_key", "product_key") VALUES ('项目验收', 'acceptance_get', 'z_markgo', 'z_markgo');

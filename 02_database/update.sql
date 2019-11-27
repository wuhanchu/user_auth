SET FOREIGN_KEY_CHECKS = 0;

truncate table sys_permission;

-- ----------------------------
-- Records of sys_permission
-- ----------------------------
INSERT INTO `sys_permission` VALUES (1, '上传待标注数据', NULL, '/api/v1/mark/project_items/upload', NULL, NULL, NULL, NULL, 'POST', 'project_item_upload');
INSERT INTO `sys_permission` VALUES (2, '下一条标注数据', NULL, '/api/v1/mark/user_items/next_item', NULL, NULL, NULL, NULL, 'GET', 'project_user_item_get_next');
INSERT INTO `sys_permission` VALUES (5, '比对报告', NULL, '/api/v1/tools/report', NULL, NULL, NULL, NULL, 'POST', 'tool_report');
INSERT INTO `sys_permission` VALUES (6, '质检数据列表', NULL, '/api/v1/mark/user_inspections', NULL, NULL, NULL, NULL, 'GET', 'project_user_inspection_get');
INSERT INTO `sys_permission` VALUES (7, '标注数据管理-添加', NULL, '/api/v1/mark/project_items', NULL, NULL, NULL, NULL, 'GET', 'project_item_post');
INSERT INTO `sys_permission` VALUES (8, '标注数据管理-批量删除', NULL, '/api/v1/mark/project_items', NULL, NULL, NULL, NULL, 'DELETE', 'project_item_get');
INSERT INTO `sys_permission` VALUES (9, '项目人员管理-更新项目人员', NULL, '/api/v1/mark/project_users', NULL, NULL, NULL, NULL, 'PUT', 'project_user_put');
INSERT INTO `sys_permission` VALUES (10, '项目人员管理-人员列表', NULL, '/api/v1/mark/project_users', NULL, NULL, NULL, NULL, 'GET', 'project_user_get');
INSERT INTO `sys_permission` VALUES (11, '我的标注/质检-列表', NULL, '/api/v1/mark/user_items', NULL, NULL, NULL, NULL, 'GET', 'project_user_item_get');
INSERT INTO `sys_permission` VALUES (12, '项目管理-列表', NULL, '/api/v1/mark/projects', NULL, NULL, NULL, NULL, 'GET', 'project_get');
INSERT INTO `sys_permission` VALUES (13, '项目管理-添加项目', NULL, '/api/v1/mark/projects', NULL, NULL, NULL, NULL, 'POST', 'project_post');
INSERT INTO `sys_permission` VALUES (17, '权限管理-列表', NULL, '/api/v1/permissions', NULL, NULL, NULL, NULL, 'GET', 'sys_permission_get');
INSERT INTO `sys_permission` VALUES (18, '权限管理-添加', NULL, '/api/v1/permissions', NULL, NULL, NULL, NULL, 'POST', 'sys_permission_post');
INSERT INTO `sys_permission` VALUES (19, 'AI服务管理-列表', NULL, '/api/v1/aiservices', NULL, NULL, NULL, NULL, 'GET', 'sys_aiservice_get');
INSERT INTO `sys_permission` VALUES (20, 'AI服务管理-添加', NULL, '/api/v1/aiservices', NULL, NULL, NULL, NULL, 'POST', 'sys_aiservice_post');
INSERT INTO `sys_permission` VALUES (21, '用户管理-列表', NULL, '/api/v1/users', NULL, NULL, NULL, NULL, 'GET', 'sys_user_put');
INSERT INTO `sys_permission` VALUES (22, '用户管理-更新', NULL, '/api/v1/users', NULL, NULL, NULL, NULL, 'POST', 'sys_user_post');
INSERT INTO `sys_permission` VALUES (25, '角色管理-列表', NULL, '/api/v1/roles', NULL, NULL, NULL, NULL, 'GET', 'sys_role_get');
INSERT INTO `sys_permission` VALUES (26, '角色管理-更新', NULL, '/api/v1/roles', NULL, NULL, NULL, NULL, 'POST', 'sys_role_post');
INSERT INTO `sys_permission` VALUES (28, '标注管理-查看音频文件', NULL, '/api/v1/mark/project_items/<id>/wav_file', NULL, NULL, NULL, NULL, 'GET', NULL);
INSERT INTO `sys_permission` VALUES (29, '项目管理-打包下载', NULL, '/api/v1/mark/projects/<id>/project_pkg', NULL, NULL, NULL, NULL, 'GET', 'project_item_audio_export');
INSERT INTO `sys_permission` VALUES (30, '用户管理-更新密码', NULL, '/api/v1/users/<id>/password', NULL, NULL, NULL, NULL, 'PUT', NULL);
INSERT INTO `sys_permission` VALUES (31, '项目人员管理-删除项目人员', NULL, '/api/v1/mark/project_users/<project_id>/<user_id>', NULL, NULL, NULL, NULL, 'DELETE', 'project_user_delete');
INSERT INTO `sys_permission` VALUES (32, '标注数据管理-查看', NULL, '/api/v1/mark/project_items/<id>', NULL, NULL, NULL, NULL, 'GET', 'project_item_get_by_id');
INSERT INTO `sys_permission` VALUES (33, '标注数据管理-更新', NULL, '/api/v1/mark/project_items/<id>', NULL, NULL, NULL, NULL, 'PUT', 'project_item_put');
INSERT INTO `sys_permission` VALUES (34, '标注数据管理-删除', NULL, '/api/v1/mark/project_items/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'project_item_delete');
INSERT INTO `sys_permission` VALUES (35, '用户项目管理-列表', NULL, '/api/v1/mark/user_projects/<user_id>', NULL, NULL, NULL, NULL, 'GET', NULL);
INSERT INTO `sys_permission` VALUES (36, '项目管理-项目详情', NULL, '/api/v1/mark/projects/<id>', NULL, NULL, NULL, NULL, 'GET', 'project_get_by_id');
INSERT INTO `sys_permission` VALUES (37, '项目管理-更新项目', NULL, '/api/v1/mark/projects/<id>', NULL, NULL, NULL, NULL, 'PUT', 'project_put');
INSERT INTO `sys_permission` VALUES (38, '项目管理-删除项目', NULL, '/api/v1/mark/projects/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'project_delete');
INSERT INTO `sys_permission` VALUES (41, '角色权限管理-角色权限列表', NULL, '/api/v1/role_permissions/<role_id>', NULL, NULL, NULL, NULL, 'GET', 'sys_role_permission_get');
INSERT INTO `sys_permission` VALUES (42, '角色权限管理-更新角色权限', NULL, '/api/v1/role_permissions/<role_id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_role_permission_put');
INSERT INTO `sys_permission` VALUES (43, '权限管理-详情', NULL, '/api/v1/permissions/<id>', NULL, NULL, NULL, NULL, 'GET', 'sys_permission_get_by_id');
INSERT INTO `sys_permission` VALUES (44, '权限管理-更新权限', NULL, '/api/v1/permissions/<id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_permission_put');
INSERT INTO `sys_permission` VALUES (45, '权限管理-删除权限', NULL, '/api/v1/permissions/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'sys_permission_delete');
INSERT INTO `sys_permission` VALUES (46, 'AI服务管理-详情', NULL, '/api/v1/aiservices/<id>', NULL, NULL, NULL, NULL, 'GET', 'sys_aiservice_get_by_id');
INSERT INTO `sys_permission` VALUES (47, 'AI服务管理-更新服务', NULL, '/api/v1/aiservices/<id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_aiservice_put');
INSERT INTO `sys_permission` VALUES (48, 'AI服务管理-删除', NULL, '/api/v1/aiservices/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'sys_aiservice_delete');
INSERT INTO `sys_permission` VALUES (50, '用户角色管理-角色详情', NULL, '/api/v1/user_roles/<user_id>', NULL, NULL, NULL, NULL, 'GET', 'sys_user_role_get');
INSERT INTO `sys_permission` VALUES (51, '用户角色管理-更新角色', NULL, '/api/v1/user_roles/<user_id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_user_role_put');
INSERT INTO `sys_permission` VALUES (52, '用户管理-详情', NULL, '/api/v1/users/<id>', NULL, NULL, NULL, NULL, 'GET', 'sys_user_get_by_id');
INSERT INTO `sys_permission` VALUES (53, '用户管理-更新用户', NULL, '/api/v1/users/<id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_user_get');
INSERT INTO `sys_permission` VALUES (54, '用户管理-删除用户', NULL, '/api/v1/users/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'sys_user_delete');
INSERT INTO `sys_permission` VALUES (58, '角色管理-详情', NULL, '/api/v1/roles/<id>', NULL, NULL, NULL, NULL, 'GET', 'sys_role_get_by_id');
INSERT INTO `sys_permission` VALUES (59, '角色管理-更新角色', NULL, '/api/v1/roles/<id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_role_put');
INSERT INTO `sys_permission` VALUES (60, NULL, NULL, '/api/v1/roles/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'sys_role_delete');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;

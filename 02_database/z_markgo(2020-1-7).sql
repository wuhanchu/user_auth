/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.1.150(内网)
 Source Server Type    : MySQL
 Source Server Version : 50643
 Source Host           : 192.168.1.150:3306
 Source Schema         : z_markgo

 Target Server Type    : MySQL
 Target Server Version : 50643
 File Encoding         : 65001

 Date: 07/01/2020 16:18:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ai_service
-- ----------------------------
DROP TABLE IF EXISTS `ai_service`;
CREATE TABLE `ai_service`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '服务名称',
  `service_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '服务地址',
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '标注类型：取值 asr：语音识别 ；ocr：图像识别',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'AI服务' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of ai_service
-- ----------------------------
INSERT INTO `ai_service` VALUES (1, '东方证券智能客服', 'http://192.168.1.150:34568/', 'asr');
INSERT INTO `ai_service` VALUES (3, '话术文本', ' ', 'asr');
INSERT INTO `ai_service` VALUES (5, '国盛证券智能见证', 'http://192.168.1.150:3998/', 'asr');
INSERT INTO `ai_service` VALUES (6, '小雷的8K', 'http://125.77.202.194:34569/\n', 'asr');
INSERT INTO `ai_service` VALUES (7, '16KTC3998', 'http://125.77.202.194:3998/', 'asr');
INSERT INTO `ai_service` VALUES (8, '独立8K', 'http://192.168.1.220:34568/', 'asr');
INSERT INTO `ai_service` VALUES (10, '16K东方证券', 'http://192.168.1.150:3667/', 'asr');
INSERT INTO `ai_service` VALUES (11, '8K通用模型小雷Linux', 'http://125.77.202.194:9392/', 'asr');
INSERT INTO `ai_service` VALUES (12, '8K通用', 'http://192.168.1.107:34568/', 'asr');
INSERT INTO `ai_service` VALUES (13, '通用16K', 'http://192.168.1.150:3667/\n', 'asr');
INSERT INTO `ai_service` VALUES (14, '江海证券', 'http://192.168.1.107:34569/\n', 'asr');
INSERT INTO `ai_service` VALUES (15, 'jt8k', 'http://192.168.1.107:34569/', 'asr');
INSERT INTO `ai_service` VALUES (16, '国盛本地生产', 'http://192.168.1.83:3998/', 'asr');
INSERT INTO `ai_service` VALUES (17, '通用16K-测试', 'http://192.168.1.150:3666/', 'asr');

-- ----------------------------
-- Table structure for mark_project
-- ----------------------------
DROP TABLE IF EXISTS `mark_project`;
CREATE TABLE `mark_project`  (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `name` varchar(800) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '项目名',
  `status` int(1) NULL DEFAULT 0 COMMENT '项目状态：0：进行中，1：暂停；2归档',
  `model_txt` varchar(5000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '默认话术文本',
  `ai_service` int(8) NULL DEFAULT NULL COMMENT '默认文本类型：1：话术文本，2. 自带机转，3.讯飞机转',
  `type` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '标注类型：asr，语音标注；ocr：图像标注',
  `plan_time` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '计划完成时间，格式:2019-07-31',
  `inspection_persent` int(3) NULL DEFAULT NULL COMMENT '质检比例:取值0-100',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `asr_score` float(5, 2) NULL DEFAULT NULL COMMENT '模型准确率',
  `remarks` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
  `frame_rate` int(2) NULL DEFAULT NULL COMMENT '音频采样率，取值范围（8,16）',
  `roles` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '角色信息',
  `marks` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '标签信息',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 165 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '标注项目' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for mark_project_items
-- ----------------------------
DROP TABLE IF EXISTS `mark_project_items`;
CREATE TABLE `mark_project_items`  (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NULL DEFAULT NULL COMMENT '项目id',
  `filepath` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '文件路径',
  `status` int(1) NULL DEFAULT 0 COMMENT '状态: 0,未分配，1已分配，2 已标注',
  `asr_txt` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '转写文本',
  `mark_txt` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '标注文本',
  `user_id` int(11) NULL DEFAULT NULL COMMENT '用户id',
  `inspection_status` int(1) NULL DEFAULT 0 COMMENT '质检状态：0未质检，1 已分配，2检通过，3质检未通过',
  `mark_time` datetime(0) NULL DEFAULT NULL COMMENT '标注时间',
  `assigned_time` datetime(0) NULL DEFAULT NULL COMMENT '分配时间',
  `inspection_time` datetime(0) NULL DEFAULT NULL COMMENT '质检时间',
  `inspection_person` int(255) NULL DEFAULT NULL COMMENT '质检人员',
  `inspection_txt` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '质检文本',
  `asr_score` float(5, 2) NULL DEFAULT NULL COMMENT '模型准确率',
  `remark` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '异常原因记录',
  `inspection_result` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '比对结果',
  `upload_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP COMMENT '上传时间',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_item_project`(`project_id`) USING BTREE,
  INDEX `fk_item_project1`(`user_id`) USING BTREE,
  INDEX `fk_item_project2`(`inspection_person`) USING BTREE,
  CONSTRAINT `fk_item_project` FOREIGN KEY (`project_id`) REFERENCES `mark_project` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_item_project1` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_item_project2` FOREIGN KEY (`inspection_person`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4317 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '语音标注条目' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for mark_project_user
-- ----------------------------
DROP TABLE IF EXISTS `mark_project_user`;
CREATE TABLE `mark_project_user`  (
  `project_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `task_num` int(11) NULL DEFAULT NULL COMMENT '总任务量',
  `mark_role` int(1) NULL DEFAULT 0 COMMENT '标注角色：0，标注人员，1质检人员',
  PRIMARY KEY (`project_id`, `user_id`) USING BTREE,
  INDEX `fk_mark_project_user2`(`user_id`) USING BTREE,
  CONSTRAINT `fk_mark_project_user1` FOREIGN KEY (`project_id`) REFERENCES `mark_project` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_mark_project_user2` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for oauth2_client
-- ----------------------------
DROP TABLE IF EXISTS `oauth2_client`;
CREATE TABLE `oauth2_client`  (
  `client_id` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `client_secret` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `issued_at` int(11) NOT NULL,
  `expires_at` int(11) NOT NULL,
  `redirect_uri` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `token_endpoint_auth_method` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `grant_type` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `response_type` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `scope` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `client_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `client_uri` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `logo_uri` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `contact` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `tos_uri` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `policy_uri` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `jwks_uri` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `jwks_text` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `i18n_metadata` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `software_id` varchar(36) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `software_version` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `ix_oauth2_client_client_id`(`client_id`) USING BTREE,
  CONSTRAINT `oauth2_client_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of oauth2_client
-- ----------------------------
INSERT INTO `oauth2_client` VALUES ('yAl9PO9sA4NKYhcrXfAOXxlD', 'DarmrCkeA04rV8t8vA4mTXhMvn7nEUweE07JgvWhEVpGsukK', 1565360863, 0, 'http://localhost:5002/api/v1/users?limit=10&offset=0', 'client_secret_basic', 'authorization_code\r\npassword', 'code', 'profile', 'markgo', 'http://localhost:5002', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2, 1);
INSERT INTO `oauth2_client` VALUES ('UvPlzkstsF76wK62EHXIfsr6', '7sgil6mSsYajaBwMuBskjHHS2OXdtekKm5HLxWqxTyqatAlv', 1565361672, 0, 'http://localhost:5002/api/me', 'client_secret_basic', 'password', 'code', 'profile', 'me', 'http://localhost:5002/api/me', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3, 1);
INSERT INTO `oauth2_client` VALUES ('7Wsu7D0TRezehTgTxD66VM7w', 'tnNZ3OS7tumq87uqgQXK0Y6bSbfeKmo7NSW3nk8wvpM9eenT', 1565429749, 0, 'https://localhost:5002', 'client_secret_basic', 'authorization_code\r\npassword', 'code', 'profile', 'markgo', 'https://localhost:5002/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 4, 1);

-- ----------------------------
-- Table structure for oauth2_code
-- ----------------------------
DROP TABLE IF EXISTS `oauth2_code`;
CREATE TABLE `oauth2_code`  (
  `code` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `client_id` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `redirect_uri` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `response_type` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `scope` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `auth_time` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `code`(`code`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `oauth2_code_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for oauth2_token
-- ----------------------------
DROP TABLE IF EXISTS `oauth2_token`;
CREATE TABLE `oauth2_token`  (
  `client_id` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `token_type` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `access_token` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `refresh_token` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `scope` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `revoked` tinyint(1) NULL DEFAULT NULL,
  `issued_at` int(11) NOT NULL,
  `expires_in` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `access_token`(`access_token`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `ix_oauth2_token_refresh_token`(`refresh_token`) USING BTREE,
  CONSTRAINT `oauth2_token_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1596 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;
;

-- ----------------------------
-- Table structure for sys_menu
-- ----------------------------
DROP TABLE IF EXISTS `sys_menu`;
CREATE TABLE `sys_menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '菜单ID\r\n            ',
  `path` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '路由路径',
  `component` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '路由组件',
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '路由名称',
  `hidden` tinyint(1) NULL DEFAULT NULL COMMENT '路由是否显示',
  `icon_cls` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '路由路径图标',
  `keep_Alive` tinyint(1) NULL DEFAULT NULL COMMENT '路由缓存组件\r\n            ',
  `require_auth` tinyint(1) NULL DEFAULT NULL COMMENT '路由验证是否需要登陆才能访问',
  `parent_id` int(11) NULL DEFAULT NULL COMMENT '父菜单ID\r\n            ',
  `op_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作人',
  `op_at` bigint(32) NULL DEFAULT NULL COMMENT '操作时间',
  `del_fg` tinyint(1) NULL DEFAULT NULL COMMENT '删除标识',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '菜单表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for sys_param
-- ----------------------------
DROP TABLE IF EXISTS `sys_param`;
CREATE TABLE `sys_param`  (
  `param_code` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '编码',
  `param_name` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '名称',
  `param_value` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '取值',
  `param_type` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '取值类型：1.字符串 ；2：字典类型 json数组格式[{key：\"\",value:\"\",desc:\"\"}]',
  `note` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '参数说明',
  PRIMARY KEY (`param_code`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'SYS_PARAM参数表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for sys_permission
-- ----------------------------
DROP TABLE IF EXISTS `sys_permission`;
CREATE TABLE `sys_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '权限名称',
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '权限描述\r\n            ',
  `url` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '路由匹配地址',
  `pid` int(11) NULL DEFAULT NULL,
  `opr_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作人',
  `opr_at` bigint(32) NULL DEFAULT NULL COMMENT '操作时间',
  `del_fg` tinyint(1) NULL DEFAULT NULL COMMENT '删除标识',
  `method` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '1，get，2.post，3.put；4，delete',
  `key` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '关联菜单字段',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 83 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '系统权限表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_permission
-- ----------------------------
INSERT INTO `sys_permission` VALUES (1, '上传待标注数据', NULL, '/api/v1/mark/project_items/upload', NULL, NULL, NULL, NULL, 'POST', 'project_item_upload');
INSERT INTO `sys_permission` VALUES (2, '下一条标注数据', NULL, '/api/v1/mark/user_items/next_item', NULL, NULL, NULL, NULL, 'GET', 'get_next_project_user_item');
INSERT INTO `sys_permission` VALUES (5, '比对报告', NULL, '/api/v1/tools/report', NULL, NULL, NULL, NULL, 'POST', 'tool_report');
INSERT INTO `sys_permission` VALUES (6, '质检数据列表', NULL, '/api/v1/mark/user_inspections', NULL, NULL, NULL, NULL, 'GET', 'project_user_inspection_get');
INSERT INTO `sys_permission` VALUES (7, '标注数据管理-添加', NULL, '/api/v1/mark/project_items', NULL, NULL, NULL, NULL, 'POST', 'project_item_post');
INSERT INTO `sys_permission` VALUES (8, '标注数据管理-批量删除', NULL, '/api/v1/mark/project_items', NULL, NULL, NULL, NULL, 'DELETE', 'project_item_del_all');
INSERT INTO `sys_permission` VALUES (9, '项目人员管理-更新项目人员', NULL, '/api/v1/mark/project_users', NULL, NULL, NULL, NULL, 'PUT', 'project_user_put');
INSERT INTO `sys_permission` VALUES (10, '项目人员管理-人员列表', NULL, '/api/v1/mark/project_users', NULL, NULL, NULL, NULL, 'GET', 'project_user_get');
INSERT INTO `sys_permission` VALUES (11, '我的标注/质检-列表', NULL, '/api/v1/mark/user_items', NULL, NULL, NULL, NULL, 'GET', 'project_user_item_get');
INSERT INTO `sys_permission` VALUES (12, '项目管理-列表', NULL, '/api/v1/mark/projects', NULL, NULL, NULL, NULL, 'GET', 'project_get');
INSERT INTO `sys_permission` VALUES (13, '项目管理-添加项目', NULL, '/api/v1/mark/projects', NULL, NULL, NULL, NULL, 'POST', 'project_post');
INSERT INTO `sys_permission` VALUES (17, '权限管理-列表', NULL, '/api/v1/permissions', NULL, NULL, NULL, NULL, 'GET', 'sys_permission_get');
INSERT INTO `sys_permission` VALUES (18, '权限管理-添加', NULL, '/api/v1/permissions', NULL, NULL, NULL, NULL, 'POST', 'sys_permission_post');
INSERT INTO `sys_permission` VALUES (19, 'AI服务管理-列表', NULL, '/api/v1/aiservices', NULL, NULL, NULL, NULL, 'GET', 'sys_aiservice_get');
INSERT INTO `sys_permission` VALUES (20, 'AI服务管理-添加', NULL, '/api/v1/aiservices', NULL, NULL, NULL, NULL, 'POST', 'sys_aiservice_post');
INSERT INTO `sys_permission` VALUES (22, '用户管理-更新', NULL, '/api/v1/users', NULL, NULL, NULL, NULL, 'POST', 'sys_user_post');
INSERT INTO `sys_permission` VALUES (25, '角色管理-列表', NULL, '/api/v1/roles', NULL, NULL, NULL, NULL, 'GET', 'role_get');
INSERT INTO `sys_permission` VALUES (26, '角色管理-更新', NULL, '/api/v1/roles', NULL, NULL, NULL, NULL, 'POST', 'sys_role_post');
INSERT INTO `sys_permission` VALUES (28, '标注管理-查看音频文件', NULL, '/api/v1/mark/project_items/<id>/wav_file', NULL, NULL, NULL, NULL, 'GET', NULL);
INSERT INTO `sys_permission` VALUES (29, '项目管理-打包下载', NULL, '/api/v1/mark/projects/<id>/project_pkg', NULL, NULL, NULL, NULL, 'GET', 'project_item_audio_export');
INSERT INTO `sys_permission` VALUES (30, '用户管理-更新密码', NULL, '/api/v1/users/<id>/password', NULL, NULL, NULL, NULL, 'PUT', NULL);
INSERT INTO `sys_permission` VALUES (31, '项目人员管理-删除项目人员', NULL, '/api/v1/mark/project_users/<project_id>/<user_id>', NULL, NULL, NULL, NULL, 'DELETE', 'project_user_delete');
INSERT INTO `sys_permission` VALUES (32, '标注数据管理-查看', NULL, '/api/v1/mark/project_items/<id>', NULL, NULL, NULL, NULL, 'GET', 'project_item_get_by_id');
INSERT INTO `sys_permission` VALUES (33, '标注数据管理-更新', NULL, '/api/v1/mark/project_items/<id>', NULL, NULL, NULL, NULL, 'PUT', 'project_item_put');
INSERT INTO `sys_permission` VALUES (34, '标注数据管理-删除', NULL, '/api/v1/mark/project_items/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'project_item_delete');
INSERT INTO `sys_permission` VALUES (35, '用户项目管理-列表', NULL, '/api/v1/mark/user_projects/<user_id>', NULL, NULL, NULL, NULL, 'GET', 'project_user_projects_get');
INSERT INTO `sys_permission` VALUES (36, '项目管理-项目详情', NULL, '/api/v1/mark/projects/<id>', NULL, NULL, NULL, NULL, 'GET', 'project_get_by_id');
INSERT INTO `sys_permission` VALUES (37, '项目管理-更新项目', NULL, '/api/v1/mark/projects/<id>', NULL, NULL, NULL, NULL, 'PUT', 'project_put');
INSERT INTO `sys_permission` VALUES (38, '项目管理-删除项目', NULL, '/api/v1/mark/projects/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'project_delete');
INSERT INTO `sys_permission` VALUES (43, '权限管理-详情', NULL, '/api/v1/permissions/<id>', NULL, NULL, NULL, NULL, 'GET', 'sys_permission_get_by_id');
INSERT INTO `sys_permission` VALUES (44, '权限管理-更新权限', NULL, '/api/v1/permissions/<id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_permission_put');
INSERT INTO `sys_permission` VALUES (45, '权限管理-删除权限', NULL, '/api/v1/permissions/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'sys_permission_delete');
INSERT INTO `sys_permission` VALUES (46, 'AI服务管理-详情', NULL, '/api/v1/aiservices/<id>', NULL, NULL, NULL, NULL, 'GET', 'sys_aiservice_get_by_id');
INSERT INTO `sys_permission` VALUES (47, 'AI服务管理-更新服务', NULL, '/api/v1/aiservices/<id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_aiservice_put');
INSERT INTO `sys_permission` VALUES (48, 'AI服务管理-删除', NULL, '/api/v1/aiservices/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'sys_aiservice_delete');
INSERT INTO `sys_permission` VALUES (50, '用户角色管理-角色详情', NULL, '/api/v1/user_roles/<user_id>', NULL, NULL, NULL, NULL, 'GET', 'sys_user_role_get');
INSERT INTO `sys_permission` VALUES (51, '用户角色管理-更新角色', NULL, '/api/v1/user_roles/<user_id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_user_role_put');
INSERT INTO `sys_permission` VALUES (52, '用户管理-详情', NULL, '/api/v1/users/<id>', NULL, NULL, NULL, NULL, 'GET', 'sys_user_get_by_id');
INSERT INTO `sys_permission` VALUES (53, '用户管理-更新用户', NULL, '/api/v1/users/<id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_user_put');
INSERT INTO `sys_permission` VALUES (54, '用户管理-删除用户', NULL, '/api/v1/users/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'sys_user_delete');
INSERT INTO `sys_permission` VALUES (58, '角色管理-详情', NULL, '/api/v1/roles/<id>', NULL, NULL, NULL, NULL, 'GET', 'sys_role_get_by_id');
INSERT INTO `sys_permission` VALUES (59, '角色管理-更新角色', NULL, '/api/v1/roles/<id>', NULL, NULL, NULL, NULL, 'PUT', 'sys_role_put');
INSERT INTO `sys_permission` VALUES (60, '角色管理-删除角色', NULL, '/api/v1/roles/<id>', NULL, NULL, NULL, NULL, 'DELETE', 'sys_role_delete');
INSERT INTO `sys_permission` VALUES (61, '角色权限组管理-获取权限组', NULL, '/api/v1/role_permission_groups/<role_id>', NULL, NULL, NULL, NULL, 'GET', NULL);
INSERT INTO `sys_permission` VALUES (62, '角色权限组管理-更新权限组', NULL, '/api/v1/role_permission_groups/<role_id>', NULL, NULL, NULL, NULL, 'PUT', NULL);
INSERT INTO `sys_permission` VALUES (63, '权限组权限管理-更新权限列表', NULL, '/api/v1/group_permissions/<permission_group_id>', NULL, NULL, NULL, NULL, 'PUT', NULL);
INSERT INTO `sys_permission` VALUES (64, '权限组权限管理-查看权限列表', NULL, '/api/v1/group_permissions/<permission_group_id>', NULL, NULL, NULL, NULL, 'GET', NULL);
INSERT INTO `sys_permission` VALUES (65, '权限组管理-查看详情', NULL, '/api/v1/permission_group/<id>', NULL, NULL, NULL, NULL, 'GET', NULL);
INSERT INTO `sys_permission` VALUES (66, '权限组管理-更新', NULL, '/api/v1/permission_group/<id>', NULL, NULL, NULL, NULL, 'PUT', NULL);
INSERT INTO `sys_permission` VALUES (67, '权限组管理-列表', NULL, '/api/v1/permission_group', NULL, NULL, NULL, NULL, 'GET', NULL);
INSERT INTO `sys_permission` VALUES (68, '权限组管理-添加', NULL, '/api/v1/permission_group', NULL, NULL, NULL, NULL, 'POST', NULL);
INSERT INTO `sys_permission` VALUES (69, '权限组管理-删除', NULL, '/api/v1/permission_group/<id>', NULL, NULL, NULL, NULL, 'DELETE', NULL);
INSERT INTO `sys_permission` VALUES (70, '功能管理-列表', NULL, '/api/v1/permission_group', NULL, NULL, NULL, NULL, 'GET', 'permission_group_get');
INSERT INTO `sys_permission` VALUES (71, '用户登陆-角色管理-列表', NULL, '/api/v1/roles', NULL, NULL, NULL, NULL, 'GET', 'login_sys_role_get');
INSERT INTO `sys_permission` VALUES (72, '用户登陆-用户角色管理-角色详情', NULL, '/api/v1/user_roles/<user_id>', NULL, NULL, NULL, NULL, 'GET', 'login_sys_user_role_get');
INSERT INTO `sys_permission` VALUES (73, '角色管理-功能分配', NULL, '/api/v1/role_permissions/<id>', NULL, NULL, NULL, NULL, 'GET', 'get_role_permissions_sys_role');
INSERT INTO `sys_permission` VALUES (74, '用户管理-列表', NULL, '/api/v1/users', NULL, NULL, NULL, NULL, 'GET', 'user_get');
INSERT INTO `sys_permission` VALUES (75, 'AI服务管理-登陆', NULL, '/api/v1/aiservices', NULL, NULL, NULL, NULL, 'GET', 'login_aiservice_get');
INSERT INTO `sys_permission` VALUES (77, '项目管理-列表-登陆', NULL, '/api/v1/mark/projects', NULL, NULL, NULL, NULL, 'GET', 'login_project_get');
INSERT INTO `sys_permission` VALUES (79, '用户管理-列表-登陆', NULL, '/api/v1/users', NULL, NULL, NULL, NULL, 'GET', 'sys_user_login');
INSERT INTO `sys_permission` VALUES (81, '我的标注-数据', NULL, '/api/v1/mark/user_projects/<user_id>', NULL, NULL, NULL, NULL, 'GET', 'project_user_projects_get');
INSERT INTO `sys_permission` VALUES (82, '标注数据管理-列表', NULL, '/api/v1/mark/project_items', NULL, NULL, NULL, NULL, 'GET', 'project_item_get');

-- ----------------------------
-- Table structure for sys_permission_group
-- ----------------------------
DROP TABLE IF EXISTS `sys_permission_group`;
CREATE TABLE `sys_permission_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `key` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '关联菜单字段',
  `parent_key` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '父节点',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 53 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_permission_group
-- ----------------------------
INSERT INTO `sys_permission_group` VALUES (4, 'AI服务管理', 'system_aiservice_get', 'system');
INSERT INTO `sys_permission_group` VALUES (5, 'AI服务管理-删除', 'system_aiservice_delete', 'system_aiservice_get');
INSERT INTO `sys_permission_group` VALUES (6, 'AI服务管理-修改服务', 'system_aiservice_put', 'system_aiservice_get');
INSERT INTO `sys_permission_group` VALUES (7, 'AI服务管理-新增', 'system_aiservice_post', 'system_aiservice_get');
INSERT INTO `sys_permission_group` VALUES (9, '上传待标注数据', 'project_item_upload', 'project_item_get');
INSERT INTO `sys_permission_group` VALUES (10, '下一条标注数据', 'project_user_item_get_next', 'project_user_item_get');
INSERT INTO `sys_permission_group` VALUES (11, '去标注', 'project_user_item_get', 'basic');
INSERT INTO `sys_permission_group` VALUES (12, '权限管理', 'system_permission_get', 'system');
INSERT INTO `sys_permission_group` VALUES (13, '权限管理-删除权限', 'system_permission_delete', 'system_permission_get');
INSERT INTO `sys_permission_group` VALUES (14, '权限管理-修改权限', 'system_permission_put', 'system_permission_get');
INSERT INTO `sys_permission_group` VALUES (15, '权限管理-新增', 'system_permission_post', 'system_permission_get');
INSERT INTO `sys_permission_group` VALUES (16, '权限管理-详情', 'system_permission_get_by_id', 'system_permission_get');
INSERT INTO `sys_permission_group` VALUES (17, '文件管理-删除', 'project_item_delete', 'project_item_get');
INSERT INTO `sys_permission_group` VALUES (18, '文件管理', 'project_item_get', 'project_list');
INSERT INTO `sys_permission_group` VALUES (19, '文件管理-修改', 'project_item_put', 'project_item_get');
INSERT INTO `sys_permission_group` VALUES (20, '文件管理-查看', 'project_item_get_by_id', 'project_item_get');
INSERT INTO `sys_permission_group` VALUES (21, '文件管理-新增', 'project_item_post', 'project_item_get');
INSERT INTO `sys_permission_group` VALUES (22, '比对报告', 'tool_report', 'tool');
INSERT INTO `sys_permission_group` VALUES (23, '用户管理-修改', 'system_user_put', 'system_user_get');
INSERT INTO `sys_permission_group` VALUES (24, '用户管理-删除用户', 'system_user_delete', 'system_user_get');
INSERT INTO `sys_permission_group` VALUES (25, '用户管理-新增', 'system_user_post', 'system_user_get');
INSERT INTO `sys_permission_group` VALUES (26, '用户管理', 'system_user_get', 'system');
INSERT INTO `sys_permission_group` VALUES (27, '用户管理-详情', 'system_user_get_by_id', 'system_user_get');
INSERT INTO `sys_permission_group` VALUES (28, '用户角色管理-修改角色', 'system_user_role_put', 'system_user_get');
INSERT INTO `sys_permission_group` VALUES (29, '用户角色管理-角色详情', 'system_user_role_get', 'system_user_get');
INSERT INTO `sys_permission_group` VALUES (30, '角色管理', 'system_role_get', 'system');
INSERT INTO `sys_permission_group` VALUES (31, '角色管理-删除角色', 'system_role_delete', 'system_role_get');
INSERT INTO `sys_permission_group` VALUES (32, '角色管理-新增', 'system_role_post', 'system_role_get');
INSERT INTO `sys_permission_group` VALUES (33, '角色管理-修改角色', 'system_role_put', 'system_role_get');
INSERT INTO `sys_permission_group` VALUES (34, '角色管理-详情', 'system_role_get_by_id', 'system_role_get');
INSERT INTO `sys_permission_group` VALUES (35, '我的质检', 'project_user_inspection_get', 'basic');
INSERT INTO `sys_permission_group` VALUES (36, '人员管理', 'project_user_get', 'project_list');
INSERT INTO `sys_permission_group` VALUES (37, '人员管理-删除项目人员', 'project_user_delete', 'project_user_get');
INSERT INTO `sys_permission_group` VALUES (38, '人员管理-分配项目人员', 'project_user_put', 'project_user_get');
INSERT INTO `sys_permission_group` VALUES (39, '我的项目', 'project_list', 'basic');
INSERT INTO `sys_permission_group` VALUES (40, '删除项目', 'project_delete', 'project_list');
INSERT INTO `sys_permission_group` VALUES (41, '打包下载', 'project_item_audio_export', 'project_list');
INSERT INTO `sys_permission_group` VALUES (42, '修改项目', 'project_put', 'project_list');
INSERT INTO `sys_permission_group` VALUES (43, '新增项目', 'project_post', 'project_list');
INSERT INTO `sys_permission_group` VALUES (44, '项目详情', 'project_get_by_id', 'project_list');
INSERT INTO `sys_permission_group` VALUES (46, '登陆', 'basic', '');
INSERT INTO `sys_permission_group` VALUES (47, '工具', 'tool', 'basic');
INSERT INTO `sys_permission_group` VALUES (48, '系统管理', 'system', 'basic');
INSERT INTO `sys_permission_group` VALUES (49, '证书', 'system_license', 'system');
INSERT INTO `sys_permission_group` VALUES (50, '项目锁定', 'project_lock', 'project_list');
INSERT INTO `sys_permission_group` VALUES (51, '功能管理', 'system_function_get', 'system');
INSERT INTO `sys_permission_group` VALUES (52, '角色管理-功能分配', 'get_role_permissions_sys_role', 'system_role_get');

-- ----------------------------
-- Table structure for sys_permission_group_rel
-- ----------------------------
DROP TABLE IF EXISTS `sys_permission_group_rel`;
CREATE TABLE `sys_permission_group_rel`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission_id` int(11) NULL DEFAULT NULL,
  `permission_group_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_perssion_id`(`permission_id`) USING BTREE,
  INDEX `fk_permission_group_id`(`permission_group_id`) USING BTREE,
  CONSTRAINT `fk_permission_group_id` FOREIGN KEY (`permission_group_id`) REFERENCES `sys_permission_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_perssion_id` FOREIGN KEY (`permission_id`) REFERENCES `sys_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 341 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_permission_group_rel
-- ----------------------------
INSERT INTO `sys_permission_group_rel` VALUES (264, 46, 4);
INSERT INTO `sys_permission_group_rel` VALUES (265, 1, 9);
INSERT INTO `sys_permission_group_rel` VALUES (266, 2, 10);
INSERT INTO `sys_permission_group_rel` VALUES (267, 11, 11);
INSERT INTO `sys_permission_group_rel` VALUES (268, 19, 4);
INSERT INTO `sys_permission_group_rel` VALUES (269, 17, 12);
INSERT INTO `sys_permission_group_rel` VALUES (270, 48, 5);
INSERT INTO `sys_permission_group_rel` VALUES (271, 47, 6);
INSERT INTO `sys_permission_group_rel` VALUES (272, 45, 13);
INSERT INTO `sys_permission_group_rel` VALUES (273, 44, 14);
INSERT INTO `sys_permission_group_rel` VALUES (274, 20, 7);
INSERT INTO `sys_permission_group_rel` VALUES (275, 18, 15);
INSERT INTO `sys_permission_group_rel` VALUES (276, 43, 16);
INSERT INTO `sys_permission_group_rel` VALUES (277, 34, 17);
INSERT INTO `sys_permission_group_rel` VALUES (278, 8, 18);
INSERT INTO `sys_permission_group_rel` VALUES (279, 33, 19);
INSERT INTO `sys_permission_group_rel` VALUES (280, 32, 20);
INSERT INTO `sys_permission_group_rel` VALUES (281, 7, 21);
INSERT INTO `sys_permission_group_rel` VALUES (282, 5, 22);
INSERT INTO `sys_permission_group_rel` VALUES (284, 54, 24);
INSERT INTO `sys_permission_group_rel` VALUES (285, 22, 25);
INSERT INTO `sys_permission_group_rel` VALUES (286, 53, 26);
INSERT INTO `sys_permission_group_rel` VALUES (287, 52, 27);
INSERT INTO `sys_permission_group_rel` VALUES (288, 51, 28);
INSERT INTO `sys_permission_group_rel` VALUES (289, 50, 29);
INSERT INTO `sys_permission_group_rel` VALUES (290, 25, 30);
INSERT INTO `sys_permission_group_rel` VALUES (291, 60, 31);
INSERT INTO `sys_permission_group_rel` VALUES (292, 26, 32);
INSERT INTO `sys_permission_group_rel` VALUES (293, 59, 33);
INSERT INTO `sys_permission_group_rel` VALUES (294, 58, 34);
INSERT INTO `sys_permission_group_rel` VALUES (295, 6, 35);
INSERT INTO `sys_permission_group_rel` VALUES (296, 10, 36);
INSERT INTO `sys_permission_group_rel` VALUES (297, 31, 37);
INSERT INTO `sys_permission_group_rel` VALUES (298, 9, 38);
INSERT INTO `sys_permission_group_rel` VALUES (299, 12, 39);
INSERT INTO `sys_permission_group_rel` VALUES (300, 38, 40);
INSERT INTO `sys_permission_group_rel` VALUES (301, 29, 41);
INSERT INTO `sys_permission_group_rel` VALUES (302, 37, 42);
INSERT INTO `sys_permission_group_rel` VALUES (303, 13, 43);
INSERT INTO `sys_permission_group_rel` VALUES (304, 36, 44);
INSERT INTO `sys_permission_group_rel` VALUES (305, 37, 50);
INSERT INTO `sys_permission_group_rel` VALUES (306, 70, 51);
INSERT INTO `sys_permission_group_rel` VALUES (309, 75, 46);
INSERT INTO `sys_permission_group_rel` VALUES (310, 70, 46);
INSERT INTO `sys_permission_group_rel` VALUES (313, 72, 46);
INSERT INTO `sys_permission_group_rel` VALUES (316, 10, 46);
INSERT INTO `sys_permission_group_rel` VALUES (317, 77, 46);
INSERT INTO `sys_permission_group_rel` VALUES (319, 36, 42);
INSERT INTO `sys_permission_group_rel` VALUES (320, 35, 21);
INSERT INTO `sys_permission_group_rel` VALUES (321, 73, 52);
INSERT INTO `sys_permission_group_rel` VALUES (325, 79, 46);
INSERT INTO `sys_permission_group_rel` VALUES (327, 25, 46);
INSERT INTO `sys_permission_group_rel` VALUES (329, 36, 11);
INSERT INTO `sys_permission_group_rel` VALUES (330, 33, 11);
INSERT INTO `sys_permission_group_rel` VALUES (332, 17, 30);
INSERT INTO `sys_permission_group_rel` VALUES (333, 35, 35);
INSERT INTO `sys_permission_group_rel` VALUES (335, 35, 46);
INSERT INTO `sys_permission_group_rel` VALUES (337, 35, 11);
INSERT INTO `sys_permission_group_rel` VALUES (338, 2, 35);
INSERT INTO `sys_permission_group_rel` VALUES (339, 36, 35);
INSERT INTO `sys_permission_group_rel` VALUES (340, 33, 35);

-- ----------------------------
-- Table structure for sys_permission_group_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_permission_group_role`;
CREATE TABLE `sys_permission_group_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NULL DEFAULT NULL,
  `permission_group_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `FK_Reference_6`(`role_id`) USING BTREE,
  INDEX `FK_Reference_8`(`permission_group_id`) USING BTREE,
  CONSTRAINT `sys_permission_group_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sys_permission_group_role_ibfk_2` FOREIGN KEY (`permission_group_id`) REFERENCES `sys_permission_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 820 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '权限角色表\r\n' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_permission_group_role
-- ----------------------------
INSERT INTO `sys_permission_group_role` VALUES (188, 1, 4);
INSERT INTO `sys_permission_group_role` VALUES (300, 7, 35);
INSERT INTO `sys_permission_group_role` VALUES (301, 7, 39);
INSERT INTO `sys_permission_group_role` VALUES (302, 7, 40);
INSERT INTO `sys_permission_group_role` VALUES (303, 7, 44);
INSERT INTO `sys_permission_group_role` VALUES (304, 7, 41);
INSERT INTO `sys_permission_group_role` VALUES (305, 7, 43);
INSERT INTO `sys_permission_group_role` VALUES (306, 7, 50);
INSERT INTO `sys_permission_group_role` VALUES (307, 7, 42);
INSERT INTO `sys_permission_group_role` VALUES (308, 7, 18);
INSERT INTO `sys_permission_group_role` VALUES (309, 7, 20);
INSERT INTO `sys_permission_group_role` VALUES (310, 7, 17);
INSERT INTO `sys_permission_group_role` VALUES (311, 7, 21);
INSERT INTO `sys_permission_group_role` VALUES (312, 7, 19);
INSERT INTO `sys_permission_group_role` VALUES (313, 7, 9);
INSERT INTO `sys_permission_group_role` VALUES (314, 7, 36);
INSERT INTO `sys_permission_group_role` VALUES (315, 7, 37);
INSERT INTO `sys_permission_group_role` VALUES (316, 7, 38);
INSERT INTO `sys_permission_group_role` VALUES (317, 7, 11);
INSERT INTO `sys_permission_group_role` VALUES (318, 7, 10);
INSERT INTO `sys_permission_group_role` VALUES (319, 7, 48);
INSERT INTO `sys_permission_group_role` VALUES (322, 7, 4);
INSERT INTO `sys_permission_group_role` VALUES (323, 7, 5);
INSERT INTO `sys_permission_group_role` VALUES (324, 7, 7);
INSERT INTO `sys_permission_group_role` VALUES (325, 7, 6);
INSERT INTO `sys_permission_group_role` VALUES (326, 7, 12);
INSERT INTO `sys_permission_group_role` VALUES (327, 7, 13);
INSERT INTO `sys_permission_group_role` VALUES (328, 7, 16);
INSERT INTO `sys_permission_group_role` VALUES (329, 7, 15);
INSERT INTO `sys_permission_group_role` VALUES (330, 7, 14);
INSERT INTO `sys_permission_group_role` VALUES (331, 7, 30);
INSERT INTO `sys_permission_group_role` VALUES (332, 7, 31);
INSERT INTO `sys_permission_group_role` VALUES (333, 7, 34);
INSERT INTO `sys_permission_group_role` VALUES (334, 7, 52);
INSERT INTO `sys_permission_group_role` VALUES (335, 7, 32);
INSERT INTO `sys_permission_group_role` VALUES (336, 7, 33);
INSERT INTO `sys_permission_group_role` VALUES (337, 7, 26);
INSERT INTO `sys_permission_group_role` VALUES (354, 7, 24);
INSERT INTO `sys_permission_group_role` VALUES (355, 7, 27);
INSERT INTO `sys_permission_group_role` VALUES (356, 7, 25);
INSERT INTO `sys_permission_group_role` VALUES (357, 7, 29);
INSERT INTO `sys_permission_group_role` VALUES (358, 7, 28);
INSERT INTO `sys_permission_group_role` VALUES (366, 1, 46);
INSERT INTO `sys_permission_group_role` VALUES (367, 1, 35);
INSERT INTO `sys_permission_group_role` VALUES (369, 1, 40);
INSERT INTO `sys_permission_group_role` VALUES (370, 1, 44);
INSERT INTO `sys_permission_group_role` VALUES (371, 1, 41);
INSERT INTO `sys_permission_group_role` VALUES (372, 1, 50);
INSERT INTO `sys_permission_group_role` VALUES (373, 1, 43);
INSERT INTO `sys_permission_group_role` VALUES (374, 1, 42);
INSERT INTO `sys_permission_group_role` VALUES (375, 1, 18);
INSERT INTO `sys_permission_group_role` VALUES (376, 1, 17);
INSERT INTO `sys_permission_group_role` VALUES (377, 1, 20);
INSERT INTO `sys_permission_group_role` VALUES (378, 1, 21);
INSERT INTO `sys_permission_group_role` VALUES (379, 1, 19);
INSERT INTO `sys_permission_group_role` VALUES (380, 1, 9);
INSERT INTO `sys_permission_group_role` VALUES (381, 1, 36);
INSERT INTO `sys_permission_group_role` VALUES (382, 1, 37);
INSERT INTO `sys_permission_group_role` VALUES (383, 1, 38);
INSERT INTO `sys_permission_group_role` VALUES (384, 1, 11);
INSERT INTO `sys_permission_group_role` VALUES (385, 1, 10);
INSERT INTO `sys_permission_group_role` VALUES (386, 1, 48);
INSERT INTO `sys_permission_group_role` VALUES (387, 1, 51);
INSERT INTO `sys_permission_group_role` VALUES (388, 1, 49);
INSERT INTO `sys_permission_group_role` VALUES (389, 1, 7);
INSERT INTO `sys_permission_group_role` VALUES (390, 1, 5);
INSERT INTO `sys_permission_group_role` VALUES (391, 1, 6);
INSERT INTO `sys_permission_group_role` VALUES (392, 1, 12);
INSERT INTO `sys_permission_group_role` VALUES (393, 1, 13);
INSERT INTO `sys_permission_group_role` VALUES (394, 1, 16);
INSERT INTO `sys_permission_group_role` VALUES (395, 1, 15);
INSERT INTO `sys_permission_group_role` VALUES (396, 1, 14);
INSERT INTO `sys_permission_group_role` VALUES (397, 1, 30);
INSERT INTO `sys_permission_group_role` VALUES (398, 1, 31);
INSERT INTO `sys_permission_group_role` VALUES (399, 1, 34);
INSERT INTO `sys_permission_group_role` VALUES (400, 1, 52);
INSERT INTO `sys_permission_group_role` VALUES (401, 1, 32);
INSERT INTO `sys_permission_group_role` VALUES (402, 1, 33);
INSERT INTO `sys_permission_group_role` VALUES (403, 1, 26);
INSERT INTO `sys_permission_group_role` VALUES (404, 1, 24);
INSERT INTO `sys_permission_group_role` VALUES (405, 1, 27);
INSERT INTO `sys_permission_group_role` VALUES (406, 1, 25);
INSERT INTO `sys_permission_group_role` VALUES (407, 1, 23);
INSERT INTO `sys_permission_group_role` VALUES (408, 1, 29);
INSERT INTO `sys_permission_group_role` VALUES (409, 1, 28);
INSERT INTO `sys_permission_group_role` VALUES (410, 1, 47);
INSERT INTO `sys_permission_group_role` VALUES (411, 1, 22);
INSERT INTO `sys_permission_group_role` VALUES (422, 2, 46);
INSERT INTO `sys_permission_group_role` VALUES (451, 3, 46);
INSERT INTO `sys_permission_group_role` VALUES (512, 7, 23);
INSERT INTO `sys_permission_group_role` VALUES (534, 9, 46);
INSERT INTO `sys_permission_group_role` VALUES (633, 2, 11);
INSERT INTO `sys_permission_group_role` VALUES (634, 2, 10);
INSERT INTO `sys_permission_group_role` VALUES (639, 7, 46);
INSERT INTO `sys_permission_group_role` VALUES (640, 1, 39);
INSERT INTO `sys_permission_group_role` VALUES (812, 7, 47);
INSERT INTO `sys_permission_group_role` VALUES (813, 7, 22);
INSERT INTO `sys_permission_group_role` VALUES (816, 9, 35);
INSERT INTO `sys_permission_group_role` VALUES (819, 3, 35);

-- ----------------------------
-- Table structure for sys_permission_menu
-- ----------------------------
DROP TABLE IF EXISTS `sys_permission_menu`;
CREATE TABLE `sys_permission_menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '菜单角色表ID\r\n            ',
  `menu_id` int(11) NULL DEFAULT NULL COMMENT '菜单ID',
  `permission_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `FK_Reference_4`(`menu_id`) USING BTREE,
  INDEX `FK_Reference_7`(`permission_id`) USING BTREE,
  CONSTRAINT `sys_permission_menu_ibfk_1` FOREIGN KEY (`menu_id`) REFERENCES `sys_menu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sys_permission_menu_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `sys_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '权限菜单表\r\n' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for sys_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_role`;
CREATE TABLE `sys_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '角色名称',
  `chinese_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '角色中文名',
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '角色描述',
  `opr_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作人',
  `opr_at` bigint(32) NULL DEFAULT NULL COMMENT '操作时间',
  `del_fg` tinyint(1) NULL DEFAULT NULL COMMENT '删除标识',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '角色表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_role
-- ----------------------------
INSERT INTO `sys_role` VALUES (1, 'superadmin', '超级管理员', '超管', NULL, 1566644576, NULL);
INSERT INTO `sys_role` VALUES (2, '标注员', '标注员', '标注员', NULL, 1566644592, NULL);
INSERT INTO `sys_role` VALUES (3, '质检员', '质检员', '质检员', NULL, 1566644605, NULL);
INSERT INTO `sys_role` VALUES (6, '客服', '客服', '客服', NULL, 1568189162, NULL);
INSERT INTO `sys_role` VALUES (7, '项目管理员', '项目管理员', '项目管理员', NULL, 1568189177, NULL);
INSERT INTO `sys_role` VALUES (8, '普通用户', '普通用户', '普通用户', NULL, 1568189316, NULL);
INSERT INTO `sys_role` VALUES (9, '客户', '客户', '客户', NULL, 1568189338, NULL);

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户姓名',
  `telephone` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户电话',
  `address` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户地址\r\n            ',
  `enabled` tinyint(1) NULL DEFAULT NULL COMMENT '账号状态',
  `loginid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户名\r\n            ',
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户密码',
  `token` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '访问凭证',
  `expires_in` int(32) NULL DEFAULT NULL COMMENT '凭证有效期',
  `login_at` bigint(32) NULL DEFAULT NULL COMMENT '登录时间',
  `login_ip` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '登录IP',
  `login_count` int(32) NOT NULL DEFAULT 1 COMMENT '登录次数',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
  `opr_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '操作人',
  `opr_at` bigint(32) NULL DEFAULT NULL COMMENT '操作时间',
  `del_fg` tinyint(1) NULL DEFAULT NULL COMMENT '1：已删除 0：未删除',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username_UNIQUE`(`loginid`) USING BTREE COMMENT '用户名唯一'
) ENGINE = InnoDB AUTO_INCREMENT = 79 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES (1, 'admin', 'admin', 'admin', 1, 'admin', '21232f297a57a5a743894a0e4a801fc3', '', 1, NULL, NULL, 1, NULL, '', NULL, NULL);

-- ----------------------------
-- Table structure for sys_user_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_role`;
CREATE TABLE `sys_user_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户角色ID\r\n            ',
  `user_id` int(11) NULL DEFAULT NULL COMMENT '用户ID\r\n            ',
  `role_id` int(11) NULL DEFAULT NULL COMMENT '角色ID\r\n            ',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `FK_Reference_2`(`role_id`) USING BTREE,
  INDEX `FK_Reference_5`(`user_id`) USING BTREE,
  CONSTRAINT `sys_user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户角色表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of sys_user_role
-- ----------------------------
INSERT INTO `sys_user_role` VALUES (1, 1, 1);


SET FOREIGN_KEY_CHECKS = 1;

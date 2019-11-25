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

 Date: 22/11/2019 15:03:11
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
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 'AI服务' ROW_FORMAT = Compact;


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
) ENGINE = InnoDB AUTO_INCREMENT = 142 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '标注项目' ROW_FORMAT = Compact;


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
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_item_project`(`project_id`) USING BTREE,
  INDEX `fk_item_project1`(`user_id`) USING BTREE,
  INDEX `fk_item_project2`(`inspection_person`) USING BTREE,
  CONSTRAINT `fk_item_project` FOREIGN KEY (`project_id`) REFERENCES `mark_project` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_item_project1` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_item_project2` FOREIGN KEY (`inspection_person`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4117 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '语音标注条目' ROW_FORMAT = Compact;

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
) ENGINE = InnoDB AUTO_INCREMENT = 857 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

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
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '系统权限表' ROW_FORMAT = Compact;

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
-- Table structure for sys_permission_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_permission_role`;
CREATE TABLE `sys_permission_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NULL DEFAULT NULL,
  `permission_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `FK_Reference_6`(`role_id`) USING BTREE,
  INDEX `FK_Reference_8`(`permission_id`) USING BTREE,
  CONSTRAINT `sys_permission_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sys_permission_role_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `sys_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 185 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '权限角色表\r\n' ROW_FORMAT = Compact;

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
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '角色表' ROW_FORMAT = Compact;


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
) ENGINE = InnoDB AUTO_INCREMENT = 71 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户表' ROW_FORMAT = Compact;

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
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户角色表' ROW_FORMAT = Compact;


# coding: utf-8
from sqlalchemy import Column, ForeignKey, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.orm import relationship
from dao.models import db
Base = db.Model


class SysPermissionGroup(Base):
    __tablename__ = 'sys_permission_group'

    id = Column(INTEGER(11), primary_key=True)
    group_name = Column(String(255))
    key = Column(String(255))
    parent_key = Column(String(255))

class SysMenu(Base):
    __tablename__ = 'sys_menu'

    id = Column(INTEGER(11), primary_key=True)
    path = Column(String(64))
    component = Column(String(64))
    name = Column(String(64))
    hidden = Column(TINYINT(1))
    icon_cls = Column(String(64))
    keep_Alive = Column(TINYINT(1))
    require_auth = Column(TINYINT(1))
    parent_id = Column(INTEGER(11))
    op_by = Column(String(32))
    op_at = Column(BIGINT(32))
    del_fg = Column(TINYINT(1))


class SysParam(Base):
    __tablename__ = 'sys_param'

    param_code = Column(String(60), primary_key=True)
    param_name = Column(String(120), nullable=False)
    param_value = Column(String(2000), nullable=False)
    param_type = Column(String(60), nullable=False)
    note = Column(String(256))


class SysPermission(Base):
    __tablename__ = 'sys_permission'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(64))
    description = Column(String(255))
    url = Column(String(64))
    pid = Column(INTEGER(11))
    opr_by = Column(String(32))
    opr_at = Column(BIGINT(32))
    del_fg = Column(TINYINT(1))
    method = Column(String(50))
    key = Column(String(255))


class SysRole(Base):
    __tablename__ = 'sys_role'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(64))
    chinese_name = Column(String(64))
    description = Column(String(255))
    opr_by = Column(String(32))
    opr_at = Column(BIGINT(32))
    del_fg = Column(TINYINT(1))


class SysUser(Base):
    __tablename__ = 'sys_user'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(32))
    telephone = Column(String(16))
    address = Column(String(64))
    enabled = Column(TINYINT(1))
    loginid = Column(String(255), unique=True)
    password = Column(String(255))
    token = Column(String(100))
    expires_in = Column(INTEGER(32))
    login_at = Column(BIGINT(32))
    login_ip = Column(String(100))
    login_count = Column(INTEGER(32), nullable=False, server_default=text("'1'"))
    remark = Column(String(255))
    opr_by = Column(String(32))
    opr_at = Column(BIGINT(32))
    del_fg = Column(TINYINT(1))
    
    def get_user_id(self):
        return self.id


class SysPermissionGroupRole(Base):
    __tablename__ = 'sys_permission_group_role'

    id = Column(INTEGER(11), primary_key=True)
    role_id = Column(ForeignKey('sys_role.id'), index=True)
    permission_group_id = Column(ForeignKey('sys_permission_group.id'), index=True)

    permission_group = relationship('SysPermissionGroup')
    role = relationship('SysRole')


class SysPermissionMenu(Base):
    __tablename__ = 'sys_permission_menu'

    id = Column(INTEGER(11), primary_key=True)
    menu_id = Column(ForeignKey('sys_menu.id'), index=True)
    permission_id = Column(ForeignKey('sys_permission.id'), index=True)

    menu = relationship('SysMenu')
    permission = relationship('SysPermission')


class SysPermissionGroupRel(Base):
    __tablename__ = 'sys_permission_group_rel'

    id = Column(INTEGER(11), primary_key=True)
    permission_id = Column(ForeignKey('sys_permission.id'), index=True)
    permission_group_id = Column(ForeignKey('sys_permission_group.id'), index=True)

    permission_group = relationship('SysPermissionGroup')
    permission = relationship('SysPermission')


class SysUserRole(Base):
    __tablename__ = 'sys_user_role'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('sys_user.id'), index=True)
    role_id = Column(ForeignKey('sys_role.id'), index=True)

    role = relationship('SysRole')
    user = relationship('SysUser')
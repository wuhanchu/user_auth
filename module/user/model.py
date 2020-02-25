# coding: utf-8

from sqlalchemy import Column, ForeignKey, String, text, cast
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.orm import relationship, foreign, remote

from extension.db import db
from module.permission.model import SysPermissionGroup

Base = db.Model

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

    permission_group = relationship('SysPermissionGroup',
                                    primaryjoin=remote(SysPermissionGroup.id) == cast(foreign(permission_group_id),
                                                                                      INET))
    role = relationship('SysRole',
                        primaryjoin=remote(SysRole.id) == cast(foreign(role_id), INET))


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

    role = relationship('SysRole',
                        primaryjoin=remote(SysRole.id) == cast(foreign(role_id), INET))
    user = relationship('SysUser',
                        primaryjoin=remote(SysUser.id) == cast(foreign(user_id), INET))

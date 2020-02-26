# coding: utf-8

from sqlalchemy import Column, ForeignKey, cast
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.orm import relationship, foreign, remote

from extension.database import db, BaseModel, db_schema
from module.permission.model import PermissionScope, Permission


class Role(BaseModel, db.Model):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True, 'schema': 'user_auth'}

    id = Column(INTEGER(11), primary_key=True)


class SysUser(BaseModel, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True, 'schema': 'user_auth'}

    id = Column(INTEGER(11), primary_key=True)

    def get_user_id(self):
        return self.id


class PermissionScopeRole(BaseModel, db.Model):
    __tablename__ = 'role_permission_group'

    id = Column(primary_key=True)
    role_id = Column(ForeignKey(db_schema + '.role.id'), index=True)
    permission_group_key = Column(ForeignKey(db_schema + '.permission_group.key'), index=True)

    permission_group = relationship(PermissionScope,
                                    primaryjoin=remote(PermissionScope.key) == foreign(permission_group_key))
    role = relationship('Role',
                        primaryjoin=remote(Role.id) == cast(foreign(role_id), INET))


class PermissionScopeRetail(db.Model, BaseModel):
    __tablename__ = 'permission_group_detail'
    __table_args__ = {'extend_existing': True, 'schema': db_schema}

    id = Column(INTEGER(11), primary_key=True)
    permission_key = Column(ForeignKey(db_schema + '.permission.key'), index=True)
    permission_scope_key = Column(ForeignKey(db_schema + '.permission_scope.key'), index=True)

    permission_scope = relationship(PermissionScope,
                                    primaryjoin=PermissionScope.key == foreign(permission_scope_key))
    permission = relationship(Permission,
                              primaryjoin=remote(Permission.key) == foreign(permission_key))


class SysUserRole(BaseModel, db.Model):
    __tablename__ = 'user_role'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey(db_schema + '.user.id'), index=True)
    role_id = Column(ForeignKey(db_schema + '.role.id'), index=True)

    role = relationship('Role',
                        primaryjoin=remote(Role.id) == foreign(role_id))
    user = relationship('SysUser',
                        primaryjoin=remote(SysUser.id) == foreign(user_id))

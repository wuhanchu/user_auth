# coding: utf-8

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship, foreign, remote

from frame.extension.database import db, BaseModel, db_schema
from module.permission.model import PermissionScope


class Role(BaseModel, db.Model):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True, 'schema': 'user_auth'}

    id = Column(INTEGER(11), primary_key=True)


class RolePermissionScope(BaseModel, db.Model):
    __tablename__ = 'role_permission_scope'

    id = Column(primary_key=True)
    role_id = Column(ForeignKey(db_schema + '.role.id'), index=True)
    permission_scope_key = Column(ForeignKey(db_schema + '.permission_scope.key'), index=True)

    permission_scope = relationship(PermissionScope,
                                    primaryjoin=remote(PermissionScope.key) == foreign(permission_scope_key))
    role = relationship('Role',
                        primaryjoin=remote(Role.id) == foreign(role_id))


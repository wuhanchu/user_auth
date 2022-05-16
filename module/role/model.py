# coding: utf-8

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship, foreign, remote

from flask_frame.extension.database import db, BaseModel, db_schema
from module.permission.model import PermissionScope


class Role(BaseModel, db.Model):
    __tablename__ = 'role'

    id = Column(INTEGER(11), primary_key=True)


class RolePermissionScope(BaseModel, db.Model):
    __tablename__ = 'role_permission_scope'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    role_id = Column(ForeignKey(db_schema + '.role.id'), index=True)
    permission_scope_key = Column(ForeignKey(db_schema + '.permission_scope.key'), index=True)

    permission_scope = relationship(PermissionScope,
                                    primaryjoin=remote(PermissionScope.key) == foreign(permission_scope_key))
    role = relationship('Role',
                        primaryjoin=remote(Role.id) == foreign(role_id))

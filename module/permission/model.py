from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship, foreign, remote

from frame.extension.database import BaseModel, db, db_schema


class PermissionScope(db.Model, BaseModel):
    __tablename__ = 'permission_scope'

    key = db.Column(db.Text, primary_key=True)


class Permission(db.Model, BaseModel):
    __tablename__ = 'permission'

    key = db.Column(db.Text, primary_key=True)


class PermissionScopeRetail(db.Model, BaseModel):
    __tablename__ = 'permission_scope_detail'
    __table_args__ = {'extend_existing': True, 'schema': db_schema}

    id = Column(INTEGER(11), primary_key=True)
    permission_key = Column(ForeignKey(db_schema + '.permission.key'), index=True)
    permission_scope_key = Column(ForeignKey(db_schema + '.permission_scope.key'), index=True)

    permission_scope = relationship(PermissionScope,
                                    primaryjoin=PermissionScope.key == foreign(permission_scope_key))
    permission = relationship(Permission,
                              primaryjoin=remote(Permission.key) == foreign(permission_key))

# coding: utf-8

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship, foreign, remote

from frame.extension.database import db, BaseModel, db_schema
from module.permission.model import PermissionScope
from module.role.model import Role


class User(BaseModel, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True, 'schema': 'user_auth'}

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)

    def get_user_id(self):
        return self.id


class UserRole(BaseModel, db.Model):
    __tablename__ = 'user_role'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey(db_schema + '.user.id'), index=True)
    role_id = Column(ForeignKey(db_schema + '.role.id'), index=True)

    role = relationship('Role',
                        primaryjoin=remote(Role.id) == foreign(role_id))
    user = relationship('User',
                        primaryjoin=remote(User.id) == foreign(user_id))


class Department(BaseModel, db.Model):
    __tablename__ = 'department'
    __table_args__ = {'extend_existing': True, 'schema': 'user_auth'}
    id = Column(INTEGER(11), primary_key=True, autoincrement=True)

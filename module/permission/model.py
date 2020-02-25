
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT

from extension.db import db

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


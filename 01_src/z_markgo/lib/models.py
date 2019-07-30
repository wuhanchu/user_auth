# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
Base = db.Model


class AiService(Base):
    __tablename__ = 'ai_service'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    service_url = Column(String(255))
    type = Column(String(255), nullable=False)


class MarkProject(Base):
    __tablename__ = 'mark_project'

    id = Column(INTEGER(8), primary_key=True)
    name = Column(String(800))
    status = Column(String(255))
    model_txt = Column(String(5000))
    ai_service = Column(INTEGER(8))
    type = Column(String(10))
    plan_time = Column(DateTime)
    inspection_persent = Column(INTEGER(3))
    create_time = Column(DateTime)
    remarks = Column(String(2000))


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

    PARAM_CODE = Column(String(60), primary_key=True)
    PARAM_NAME = Column(String(120), nullable=False)
    PARAM_GROUP = Column(String(120))
    PARAM_VALUE = Column(String(2000), nullable=False)
    PARAM_TYPE = Column(String(60), nullable=False)
    NOTE = Column(String(256))


class SysParamCode(Base):
    __tablename__ = 'sys_param_code'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(50), nullable=False)
    value = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    remark = Column(String(250))
    opr_by = Column(String(32))
    opr_at = Column(BIGINT(32))
    del_fg = Column(TINYINT(1))


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
    username = Column(String(255))
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


class MarkProjectUser(Base):
    __tablename__ = 'mark_project_user'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('sys_user.id'), index=True)
    project_id = Column(ForeignKey('mark_project.id'), index=True)

    project = relationship('MarkProject')
    user = relationship('SysUser')


class MarkVoiceItem(Base):
    __tablename__ = 'mark_voice_items'

    id = Column(INTEGER(8), primary_key=True)
    project_id = Column(ForeignKey('mark_project.id'), index=True)
    filename = Column(String(255))
    status = Column(INTEGER(1), server_default=text("'0'"))
    asr_txt = Column(String(255))
    mark_txt = Column(String(255))
    user_id = Column(INTEGER(11))
    inspection_type = Column(INTEGER(1))
    mark_time = Column(DateTime)
    assigned_time = Column(DateTime)
    inspection_time = Column(DateTime)

    project = relationship('MarkProject')


class SysPermissionMenu(Base):
    __tablename__ = 'sys_permission_menu'

    id = Column(INTEGER(11), primary_key=True)
    menu_id = Column(ForeignKey('sys_menu.id'), index=True)
    permission_id = Column(ForeignKey('sys_permission.id'), index=True)

    menu = relationship('SysMenu')
    permission = relationship('SysPermission')


class SysPermissionRole(Base):
    __tablename__ = 'sys_permission_role'

    id = Column(INTEGER(11), primary_key=True)
    role_id = Column(ForeignKey('sys_role.id'), index=True)
    permission_id = Column(ForeignKey('sys_permission.id'), index=True)

    permission = relationship('SysPermission')
    role = relationship('SysRole')


class SysUserRole(Base):
    __tablename__ = 'sys_user_role'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('sys_user.id'), index=True)
    role_id = Column(ForeignKey('sys_role.id'), index=True)

    role = relationship('SysRole')
    user = relationship('SysUser')

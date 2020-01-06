# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, Text, text,Float
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
    status = Column(INTEGER(1), server_default=text("'0'"))
    model_txt = Column(String(5000))
    ai_service = Column(INTEGER(8))
    type = Column(String(10))
    plan_time = Column(String(20))
    inspection_persent = Column(INTEGER(3))
    create_time = Column(DateTime)
    asr_score = Column(Float(5))
    remarks = Column(String(2000))
    frame_rate = Column(INTEGER(2))
    roles = Column(String(500))
    marks = Column(String(500))

class MarkProjectItem(Base):
    __tablename__ = 'mark_project_items'

    id = Column(INTEGER(8), primary_key=True)
    project_id = Column(ForeignKey('mark_project.id'), index=True)
    filepath = Column(String(255))
    status = Column(INTEGER(1), server_default=text("'0'"))
    asr_txt = Column(Text)
    mark_txt = Column(Text)
    user_id = Column(ForeignKey('sys_user.id'), index=True)
    inspection_status = Column(INTEGER(1), server_default=text("'0'"))
    upload_time = Column(DateTime)
    mark_time = Column(DateTime)
    assigned_time = Column(DateTime)
    inspection_time = Column(DateTime)
    inspection_person = Column(ForeignKey('sys_user.id'), index=True)
    inspection_txt = Column(Text)
    asr_score = Column(Float(5))
    remark = Column(String(500))
    inspection_result = Column(Text)

    sys_user = relationship('SysUser', primaryjoin='MarkProjectItem.inspection_person == SysUser.id')
    project = relationship('MarkProject')
    user = relationship('SysUser', primaryjoin='MarkProjectItem.user_id == SysUser.id')


class MarkProjectUser(Base):
    __tablename__ = 'mark_project_user'

    project_id = Column(ForeignKey('mark_project.id'), primary_key=True, nullable=False)
    user_id = Column(ForeignKey('sys_user.id'), primary_key=True, nullable=False, index=True)
    task_num = Column(INTEGER(11))
    mark_role = Column(INTEGER(1), server_default=text("'0'"))

    project = relationship('MarkProject')
    user = relationship('SysUser')

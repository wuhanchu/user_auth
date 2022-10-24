from flask_frame.extension.database import db, BaseModel


class Config(db.Model, BaseModel):
    """配置表"""

    __tablename__ = "config"

    class KEY:
        register_switch = "register_switch"  # 是否允许注册

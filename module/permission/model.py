from extension.db import db, db_schema, BaseModel


class PermissionScope(db.Model, BaseModel):
    key = db.Column(db.Text, primary_key=True)

    __tablename__ = 'permission_scope'
    __table_args__ = {'extend_existing': True, 'schema': db_schema}



class Permission(db.Model, BaseModel):
    key = db.Column(db.Text, primary_key=True)

    __tablename__ = 'permission'
    __table_args__ = {'extend_existing': True, 'schema': db_schema}

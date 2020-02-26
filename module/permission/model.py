from extension.database import db, db_schema, BaseModel


class PermissionScope(db.Model, BaseModel):
    __tablename__ = 'permission_scope'

    key = db.Column(db.Text, primary_key=True)


class Permission(db.Model, BaseModel):
    __tablename__ = 'permission'

    key = db.Column(db.Text, primary_key=True)

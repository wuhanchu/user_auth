from frame.extension.database import db, BaseModel


class License(db.Model, BaseModel):
    __tablename__ = 'license'

    product_key = db.Column(db.Text, primary_key=True)

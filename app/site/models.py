from app import db
from sqlalchemy import and_

class Templates(db.Model):
    __tablename__ = 'templates'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    author = db.Column(db.String(100))
    type = db.Column(db.String(100))
    active = db.Column(db.Boolean(), default=0)

    def get_active(type):
        return Templates.query.filter(and_(Templates.type==type, Templates.active==1)).first()

    @classmethod
    def all(cls):
        return db.session.query(cls).all()


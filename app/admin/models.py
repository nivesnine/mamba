from app import db
from sqlalchemy import and_

# Create the Models
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text())
    published = db.Column(db.Boolean(), default=0)

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    html = db.Column(db.Text())
    history = db.Column(db.Text())
    published = db.Column(db.Boolean(), default=0)

    def get_home_page():
        home_page = Page.query.filter(and_(Page.slug=='home', Page.published==1)).first()
        return home_page if home_page else None

    def get_page(slug):
        return Page.query.filter(Page.slug==slug).first()

    def get_pages():
        return Page.query.all()

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

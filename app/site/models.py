from app import db
from sqlalchemy import and_
from app.auth.models import User

class Themes(db.Model):
    __tablename__ = 'themes'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    author = db.Column(db.String(100))
    type_ = db.Column(db.String(100))
    active = db.Column(db.Boolean(), default=0)

    def get_active(type):
        return str(db.session.query(Themes.slug).filter(and_(Themes.type_==type, Themes.active==1)).first()[0])

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

class PostComment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer(), primary_key=True)
    comment = db.Column(db.Text())
    writen_by = db.Column(db.Integer(), db.ForeignKey('users.id'))
    post = db.Column(db.Integer(), db.ForeignKey('posts.id'))
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    published = db.Column(db.Boolean(), default=0)
    viewed = db.Column(db.Boolean(), default=0)

    def get_author(self):
        if self.writen_by:
            user = User.query.get(self.writen_by)
            if user:
                return user.get_display_name()
        return 'Unknown'

    def get_new_comments():
        return PostComment.query.filter_by(viewed = 0).count()

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

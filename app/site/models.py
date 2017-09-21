from app import application, db
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

    @classmethod
    def get_active(cls, type_):
        return str(db.session.query(Themes.slug).filter(and_(Themes.type_ == type_, Themes.active == 1)).first()[0])

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

    @classmethod
    def get_new_comments(cls):
        return PostComment.query.filter_by(viewed=0).count()

    @classmethod
    def get_sortable_list(cls, order, direction, page):
        per_page = application.config["ADMIN_PER_PAGE"]
        return PostComment.query.order_by(order + ' ' + direction).paginate(page, per_page, error_out=False)

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

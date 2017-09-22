from app import application, db
from sqlalchemy import and_
from app.auth.models import User
from app.site.models import PostComment, Settings


# Create the Models
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    text = db.Column(db.Text())
    published = db.Column(db.Boolean(), default=0)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    writen_by = db.Column(db.Integer(), db.ForeignKey('users.id'))
    comments = db.relationship('PostComment', backref='posts', lazy='joined')

    def get_author(self):
        if self.writen_by:
            user = User.query.get(self.writen_by)
            if user:
                return user.get_display_name()
        return 'Unknown'

    def comment_count(self):
        return PostComment.query.filter(and_(PostComment.post == self.id, PostComment.published == 1)).count()

    @classmethod
    def get_blog(cls, page):
        per_page = Settings().get_blog_per_page()
        order = Settings().get_blog_order()
        return Post.query.filter(Post.published == 1).order_by(('posts_id {}'.format(order)))\
            .paginate(page, per_page, error_out=False)

    @classmethod
    def get_by_slug(cls, slug):
        return Post.query.filter_by(slug=slug).first()

    @classmethod
    def get_sortable_list(cls, order, direction, page):
        per_page = application.config["ADMIN_PER_PAGE"]
        return Post.query.order_by(order + ' ' + direction).paginate(page, per_page, error_out=False)

    @classmethod
    def all(cls):
        return db.session.query(cls).all()


class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    css = db.Column(db.Text())
    js = db.Column(db.Text())
    html = db.Column(db.Text())
    history = db.Column(db.Text())
    published = db.Column(db.Boolean(), default=0)

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    @classmethod
    def get_sortable_list(cls, order, direction, page):
        per_page = application.config["ADMIN_PER_PAGE"]
        return cls.query.order_by(order + ' ' + direction).paginate(page, per_page, error_out=False)

    @classmethod
    def get_home_page(cls):
        slug = Settings().get_home_page()
        home_page = cls.query.filter(and_(Page.slug == slug, Page.published == 1)).first()
        return home_page if home_page else None

    @classmethod
    def get_page(cls, slug):
        return cls.query.filter(Page.slug == slug).first()

    @classmethod
    def get_published_pages(cls):
        return cls.query.filter_by(published=1).all()

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

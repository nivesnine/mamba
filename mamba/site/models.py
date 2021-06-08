from flask import current_app as app
from sqlalchemy import and_, asc, desc

from mamba import db
from mamba.auth.models import User


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

    def __repr__(self):
        return self.title

    def get_id(self):
        return self.id

    @classmethod
    def get_sortable_list(cls, order, direction, page):
        per_page = app.config["ADMIN_PER_PAGE"]
        if direction == 'desc':
            o = desc(order)
        else:
            o = asc(order)
        return cls.query.order_by(o).paginate(page, per_page, error_out=False)

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
    def get_by_slug(cls, slug):
        return Page.query.filter_by(slug=slug).first()

    @classmethod
    def all(cls):
        return db.session.query(cls).all()


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

    def __str__(self):
        return self.title

    def get_id(self):
        return self.id

    def get_slug(self):
        return self.slug

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
        if order == 'desc':
            o = desc('posts_id')
        else:
            o = asc('posts_id')
        return Post.query.filter(Post.published == 1).order_by(o) \
            .paginate(page, per_page, error_out=False)

    @classmethod
    def get_by_slug(cls, slug):
        return Post.query.filter_by(slug=slug).first()

    @classmethod
    def get_by_id(cls, page_id):
        return db.session.query(cls).get(page_id)

    @classmethod
    def get_sortable_list(cls, order, direction, page):
        per_page = app.config["ADMIN_PER_PAGE"]
        if direction == 'desc':
            o = desc(order)
        else:
            o = asc(order)
        return Post.query.order_by(o).paginate(page, per_page, error_out=False)

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
    published = db.Column(db.Boolean(), default=1)
    viewed = db.Column(db.Boolean(), default=1)

    def get_id(self):
        return self.id

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
        per_page = app.config["ADMIN_PER_PAGE"]
        if direction == 'desc':
            o = desc(order)
        else:
            o = asc(order)
        return PostComment.query.order_by(o).paginate(page, per_page, error_out=False)

    @classmethod
    def all(cls):
        return db.session.query(cls).all()


class Settings(db.Model):
    __tablename__ = 'settings'

    id = db.Column(db.Integer(), primary_key=True)
    site_name = db.Column(db.String(255))
    use_site_logo = db.Column(db.Boolean())
    site_logo_url = db.Column(db.String(255))
    home_page = db.Column(db.String(100))
    posts_per_page = db.Column(db.Integer())
    blog_sort = db.Column(db.String(6))

    @classmethod
    def get_name_or_logo(cls):
        use_logo = cls.get_use_site_logo()
        if use_logo:
            return "<img src='{}' class='logo'>".format(cls.get_site_logo_url())
        else:
            return cls.get_settings().site_name

    @classmethod
    def get_name(cls):
        return cls.get_settings().site_name

    @classmethod
    def get_use_site_logo(cls):
        return cls.get_settings().use_site_logo

    @classmethod
    def get_site_logo_url(cls):
        return cls.get_settings().site_logo_url

    @classmethod
    def get_home_page(cls):
        return cls.get_settings().home_page

    @classmethod
    def get_blog_per_page(cls):
        return cls.get_settings().posts_per_page

    @classmethod
    def get_blog_order(cls):
        return cls.get_settings().blog_sort

    @classmethod
    def get_settings(cls):
        return cls.query.get(1)


class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer(), primary_key=True)
    menu = db.Column(db.Text())

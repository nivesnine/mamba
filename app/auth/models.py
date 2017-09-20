from app import db
from flask_security import RoleMixin
from flask_login import UserMixin
from sqlalchemy.sql import and_
from sqlalchemy.orm import column_property

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))


class Role(RoleMixin, db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __eq__(self, other):
        return (self.name == other or
                self.name == getattr(other, 'name', None))

    def __ne__(self, other):
        return (self.name != other and
                self.name != getattr(other, 'name', None))

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name.replace('_', ' ')

    def get_role(name):
        return Role.query.filter_by(name=name).first()

    @classmethod
    def all(cls):
        return db.session.query(cls).all()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    full_name = column_property(first_name + " " + last_name)
    display_name = db.Column(db.String(255), default='email')
    alias = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=1)
    registered_at = db.Column(db.DateTime(), default=db.func.current_timestamp())
    roles = db.relationship('Role', secondary=roles_users,
                        backref=db.backref('users', lazy='dynamic'))
    posts = db.relationship('Post', backref='users', lazy='joined')
    comments = db.relationship('PostComment', backref='users', lazy='joined')
    registered_ip = db.Column(db.String(255))
    last_login_ip = db.Column(db.String(255))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get_roles(self):
        return self.roles

    def get_display_name(self):

        def get_display_name_type(x):
            return {
                        'first_name': self.first_name,
                        'full_name': self.full_name
                    }.get(x, self.alias)

        return get_display_name_type(self.display_name)

    def get_user_by_email(email):
        return User.query.filter_by(email = email).first() 

    def is_admin(self):
        return True if 'admin' in self.roles else False

    def has_role(self, role):
        return True if role in self.roles else False

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    @classmethod
    def all(cls):
        return db.session.query(cls).all()



from app import db
from app.auth.models import User, Role, roles_users
from app.admin.models import Post, Page
from app.site.models import Themes
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy

user = User()
user.display_name = 'admin'
user.email = 'admin@example.com'
user.password = generate_password_hash('admin')

role = Role()
role.name = 'admin'
role.description = 'top level admin role'
db.session.add(role)

user.roles.append(role)
db.session.add(user)
db.session.commit()

role = Role()
role.name = 'editor'
role.description = 'can edit pages and posts'
db.session.add(role)
db.session.commit()

role = Role()
role.name = 'writer'
role.description = 'can create pages and posts'
db.session.add(role)
db.session.commit()

post = Post()
post.title = 'Hello World'
post.text = 'This is your first blog post!'
post.published = 1
db.session.add(post)
db.session.commit()

page = Page()
page.title = 'About'
page.slug = 'about'
page.history = 'Example'
page.html = '<div class="ui one column grid text container"><h1 class="ui header">This is an about page example!</h1></div>'
page.published = 1
db.session.add(page)
db.session.commit()


template = Themes()
template.name = 'Default Site'
template.slug = 'default'
template.author = 'default'
template.type_ = 'site'
template.active = 1
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Default Auth'
template.slug = 'default'
template.author = 'default'
template.type_ = 'auth'
template.active = 1
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Default Admin'
template.slug = 'default'
template.type_ = 'admin'
template.author = 'default'
template.active = 1
db.session.add(template)
db.session.commit()

from mamba import db
from mamba.auth.models import User, Role
from mamba.site.models import Settings, Post, Page, Menu
from werkzeug.security import generate_password_hash

settings = Settings()
settings.site_name = 'My Site'
settings.use_site_logo = 0
settings.home_page = 'blog'
settings.posts_per_page = 10
settings.blog_sort = 'desc'
db.session.add(settings)
db.session.commit()

user = User()
user.display_name = 'alias'
user.email = 'admin@example.com'
user.alias = 'Admin'

user.password = generate_password_hash('admin')

role = Role()
role.name = 'admin'
role.description = 'top level admin role'
db.session.add(role)
user.roles.append(role)
db.session.commit()

role = Role()
role.name = 'editor'
role.description = 'can edit pages and posts'
db.session.add(role)
user.roles.append(role)
db.session.commit()

role = Role()
role.name = 'writer'
role.description = 'can create pages and posts'
db.session.add(role)
user.roles.append(role)
db.session.add(user)
db.session.commit()

post = Post()
post.title = 'Hello World'
post.slug = 'hello-world'
post.text = 'This is your first blog post!'
post.published = 1
post.writen_by = 1
db.session.add(post)
db.session.commit()

post = Post()
post.title = 'Long Hello'
post.slug = 'long-hello'
post.text = '<p>This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            '</p><p>This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            '</p><p>This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... ' \
            'This is a long post... it will get truncated... This is a long post... it will get truncated... </p>'
post.published = 1
post.writen_by = 1
db.session.add(post)
db.session.commit()

page = Page()
page.title = 'About'
page.slug = 'about'
page.history = 'Example'
page.html = '<div class="ui one column grid text container"><h1>This is an about page example!</h1></div>'
page.published = 1
db.session.add(page)
db.session.commit()

main_menu = Menu()
main_menu.menu = '<a class="item inverted" href="/about">About</a> <div class="ui dropdown item"> About<i ' \
                 'class="dropdown icon" aria-hidden="true"></i><div class="menu"><a class="item" href="/about">About ' \
                 'Us</a></div></div> '
db.session.add(main_menu)
db.session.commit()

mobile_menu = Menu()
mobile_menu.menu = '<a class="item inverted" href="/about">About</a><div class="ui inverted accordion item"><div ' \
                   'class="title">About<i class="dropdown icon"></i></div><div class="content"><a class="item" ' \
                   'href="/about">About Us</a></div></div> '
db.session.add(mobile_menu)
db.session.commit()

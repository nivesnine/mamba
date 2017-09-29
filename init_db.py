from app import db
from app.auth.models import User, Role
from app.site.models import Themes, Settings, Post, Page, ThemeAdminPage, ThemeOption
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

template = Themes()
template.name = 'Basic Semantic-ui Site'
template.slug = 'basic-semantic-ui'
template.author = 'default'
template.type_ = 'site'
template.active = 1
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Semantic-ui Auth'
template.slug = 'basic-semantic-ui'
template.author = 'default'
template.type_ = 'auth'
template.active = 1
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Semantic-ui Admin'
template.slug = 'basic-semantic-ui'
template.type_ = 'admin'
template.author = 'default'
template.active = 1
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Semantic-ui Error'
template.slug = 'basic-semantic-ui'
template.type_ = 'error'
template.author = 'default'
template.active = 1
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Foundation Site'
template.slug = 'basic-foundation'
template.author = 'default'
template.type_ = 'site'
template.active = 0
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Foundation Auth'
template.slug = 'basic-foundation'
template.author = 'default'
template.type_ = 'auth'
template.active = 0
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Foundation Admin'
template.slug = 'basic-foundation'
template.type_ = 'admin'
template.author = 'default'
template.active = 0
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Foundation Error'
template.slug = 'basic-foundation'
template.type_ = 'error'
template.author = 'default'
template.active = 0
db.session.add(template)
db.session.commit()


template = Themes()
template.name = 'Basic Bootstrap Site'
template.slug = 'basic-bootstrap'
template.author = 'default'
template.type_ = 'site'
template.active = 0
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Bootstrap Auth'
template.slug = 'basic-bootstrap'
template.author = 'default'
template.type_ = 'auth'
template.active = 0
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Bootstrap Admin'
template.slug = 'basic-bootstrap'
template.type_ = 'admin'
template.author = 'default'
template.active = 0
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Bootstrap Error'
template.slug = 'basic-bootstrap'
template.type_ = 'error'
template.author = 'default'
template.active = 0
db.session.add(template)
db.session.commit()


template = Themes()
template.name = 'Basic Materialize Site'
template.slug = 'basic-materialize'
template.author = 'default'
template.type_ = 'site'
template.active = 0
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Materialize Auth'
template.slug = 'basic-materialize'
template.author = 'default'
template.type_ = 'auth'
template.active = 0
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Materialize Admin'
template.slug = 'basic-materialize'
template.type_ = 'admin'
template.author = 'default'
template.active = 0
db.session.add(template)
db.session.commit()

template = Themes()
template.name = 'Basic Materialize Error'
template.slug = 'basic-materialize'
template.type_ = 'error'
template.author = 'default'
template.active = 0
db.session.add(template)
db.session.commit()

theme_admin_id = ThemeAdminPage.register_admin_page('basic-semantic-ui', 'Test Admin')
ThemeOption.register_theme_options(theme_admin_id, 'Facebook URL')
ThemeOption.register_theme_options(theme_admin_id, 'G+ URL')
ThemeOption.register_theme_options(theme_admin_id, 'LinkedIn URL')

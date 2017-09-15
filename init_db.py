from app import db
from app.auth.models import User, Role
from app.admin.models import Post, Page
from flask_security import SQLAlchemyUserDatastore
from werkzeug.security import generate_password_hash

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

email = 'admin'
encrypted_password = generate_password_hash('admin')

user_datastore.find_or_create_role(name='admin', description='Admin')
user_datastore.create_user(email=email, password=encrypted_password)

db.session.commit()

user_datastore.add_role_to_user(email, 'admin')

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


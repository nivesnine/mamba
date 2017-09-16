from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import flask_login as login

def check_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not login.current_user.is_authenticated:
            return redirect(url_for('auth.login_view'))
        return func(*args, **kwargs)
    return decorated_function

def check_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not login.current_user.is_admin():
            return redirect(url_for('site.index'))
        return func(*args, **kwargs)
    return decorated_function

# Define the WSGI application object
application = Flask(__name__)

# Configurations
application.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(application)

# error handling
@application.errorhandler(404)
def page_not_found(e):
    return render_template("error/error_template.html", status_code=404), 404


@application.errorhandler(500)
def server_error(e):
    return render_template("error_template.html", status_code=500), 500


# Import a module / component using its blueprint handler variable (mod_auth)
from app.site.controllers import site as site_module
from app.admin.controllers import admin as admin_module
from app.auth.controllers import auth as auth_module

# Register blueprint(s)
application.register_blueprint(site_module)
application.register_blueprint(admin_module)
application.register_blueprint(auth_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

@application.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


from app.admin.models import Page
@application.context_processor
def insert_pages():
    return {'pages': Page.get_pages()}

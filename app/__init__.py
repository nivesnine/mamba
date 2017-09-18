from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_htmlmin import HTMLMIN
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

def has_role(role):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not login.current_user.has_role(role):
                return redirect(url_for('site.index'))
            return func(*args, **kwargs)
        return decorated_function
    return decorator
    
# Define the WSGI application object
application = Flask(__name__)

# Configurations
application.config.from_object('config')

HTMLMIN(application)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(application)

# error handling
@application.errorhandler(404)
def page_not_found(e):
    return render_template("error/error_template.html", status_code=404), 404


@application.errorhandler(405)
def bad_request_error(e):
    return render_template("error/error_template.html", status_code=405), 405


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

from app.site.models import PostComment
@application.context_processor
def get_new_comments():
    return {'new_comments': PostComment.get_new_comments()}

#custom filters
@application.template_filter('truncate_after_tag')
def truncate_after_tag(text, target_length):
    last_closing_tag_begining = text.find('</', target_length)
    end = text.find('>', last_closing_tag_begining)
    new_text = text[:end + 1]
    if len(new_text) == 0:
        return text
    return new_text


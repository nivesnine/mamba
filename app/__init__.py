from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_htmlmin import HTMLMIN
from functools import wraps
import flask_login as login


def create_app(TESTING=False):
    application = Flask(__name__)
    application.config.from_object('config')
    application.config['TESTING'] = TESTING
    return application

application = create_app()

HTMLMIN(application)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(application)


# custom decorators
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


# Import a module / component using its blueprint handler variable (mod_auth)
from app.site.controllers import site as site_module
from app.auth.controllers import auth as auth_module
from app.admin.controllers import admin as admin_module

# Register blueprint(s)
application.register_blueprint(site_module)
application.register_blueprint(auth_module)
application.register_blueprint(admin_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

# error handling
from app.site.models import Themes


@application.errorhandler(404)
def page_not_found(e):
    template_path = Themes.get_active()
    return render_template(template_path + "/error/error_template.html", status_code=404, error=e), 404


@application.errorhandler(405)
def bad_request_error(e):
    template_path = Themes.get_active()
    return render_template(template_path + "/error/error_template.html", status_code=405, error=e), 405


from app.site.models import PostComment, Settings, Page, ThemeAdminPage, ThemeOption


# getters for templates
@application.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@application.context_processor
def insert_pages():
    return {'menu_pages': Page.all()}


@application.context_processor
def insert_theme_admin():
    return {'theme_admin': ThemeAdminPage.all()}


@application.context_processor
def get_theme_options():
    def get_theme_option(theme_option):
        return ThemeOption.get_option(theme_option)
    return {'theme_option': get_theme_option}


@application.context_processor
def get_new_comments():
    return {'new_comments': PostComment.get_new_comments()}


@application.context_processor
def get_site_name():
    return {'site_name': Settings().get_site_name()}


@application.context_processor
def get_older_newer():
    sort_order = Settings().get_blog_order()
    order = 0
    if sort_order == 'desc':
        order = 1
    return {'sort_order': order}


# custom filters
@application.template_filter('truncate_after_tag')
def truncate_after_tag(text, target_length):
    last_closing_tag_beginning = text.find('</', target_length)
    end = text.find('>', last_closing_tag_beginning)
    new_text = text[:end + 1]
    if len(new_text) == 0:
        return text
    return new_text

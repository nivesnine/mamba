from flask import Flask
from flask_htmlmin import HTMLMIN
from flask_sqlalchemy import SQLAlchemy

__version__ = (0, 0, 1, 'alpha')


def create_app(TESTING=False):
    app = Flask(__name__)
    app.config.from_object('config')
    app.config['TESTING'] = TESTING

    return app


application = app = create_app()
db = SQLAlchemy(app)

HTMLMIN(app)

from app.blueprints import register_blueprints

register_blueprints(app)

db.create_all()

from app.helpers import filters, processors
from app import decorators, error_handlers
from app.site.models import Themes


@application.errorhandler(404)
def page_not_found(e):
    template_path = Themes.get_active()
    return render_template(template_path + "/error/error_template.html", status_code=404, error=e), 404


@application.errorhandler(405)
def bad_request_error(e):
    template_path = Themes.get_active()
    return render_template(template_path + "/error/error_template.html", status_code=405, error=e), 405


from app.site.models import PostComment, Settings, Page, ThemeAdminPage, ThemeOption, Menu


# getters for templates
@application.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@application.context_processor
def insert_pages():
    menu = Menu.query.get(1).menu
    return {'menu_pages': menu}


@application.context_processor
def insert_mobile_pages():
    menu = Menu.query.get(2).menu
    return {'mobile_menu_pages': menu}


@application.context_processor
def theme_admin_pages():
    try:
        roles_obj = login.current_user.get_roles()
    except:
        return {'theme_admin_pages': ''}
    roles = []
    for role in roles_obj:
        roles.append(role.name)
    return {'theme_admin_pages': ThemeAdminPage.get_allowed_pages(roles)}


@application.context_processor
def get_theme_options():
    def get_theme_option(theme_option):
        return ThemeOption.get_option(theme_option)
    return {'theme_option': get_theme_option}


@application.context_processor
def get_new_comments():
    return {'new_comments': PostComment.get_new_comments()}


@application.context_processor
def get_site_name_or_logo():
    return {'site_name_or_logo': Settings().get_name_or_logo()}


@application.context_processor
def get_site_name():
    return {'site_name': Settings().get_name()}


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

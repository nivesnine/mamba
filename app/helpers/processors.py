import flask_login as login
from datetime import datetime

from app import app
from app.site.models import Page, ThemeAdminPage, ThemeOption, PostComment, Settings


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.context_processor
def insert_pages():
    return {'menu_pages': Page.all()}


@app.context_processor
def theme_admin_pages():
    try:
        roles_obj = login.current_user.get_roles()
    except:
        return {'theme_admin_pages': ''}
    roles = []
    for role in roles_obj:
        roles.append(role.name)
    return {'theme_admin_pages': ThemeAdminPage.get_allowed_pages(roles)}


@app.context_processor
def get_theme_options():
    def get_theme_option(theme_option):
        return ThemeOption.get_option(theme_option)

    return {'theme_option': get_theme_option}


@app.context_processor
def get_new_comments():
    return {'new_comments': PostComment.get_new_comments()}


@app.context_processor
def get_site_name_or_logo():
    return {'site_name_or_logo': Settings().get_name_or_logo()}


@app.context_processor
def get_site_name():
    return {'site_name': Settings().get_name()}


@app.context_processor
def get_older_newer():
    sort_order = Settings().get_blog_order()
    order = 0
    if sort_order == 'desc':
        order = 1
    return {'sort_order': order}

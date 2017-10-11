from datetime import datetime

from app.site.models import Menu, ThemeOption, PostComment, Settings
from app import app


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.context_processor
def insert_pages():
    menu = Menu.query.get(1).menu
    return {'menu_pages': menu}


@app.context_processor
def insert_mobile_pages():
    menu = Menu.query.get(2).menu
    return {'mobile_menu_pages': menu}


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

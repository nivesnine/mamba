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

from app.helpers import filters, processors, decorators, error_handlers

from app.admin.controllers import admin as admin_module
from app.auth.controllers import auth as auth_module
from app.site.controllers import site as site_module


def register_blueprints(app):
    app.register_blueprint(site_module)
    app.register_blueprint(auth_module)
    app.register_blueprint(admin_module)

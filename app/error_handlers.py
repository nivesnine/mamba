from flask import render_template

from app.site.models import Themes
from app import app


@app.errorhandler(404)
def page_not_found(e):
    template_path = Themes.get_active()
    return render_template(template_path + "/error/error_template.html", status_code=404, error=e), 404


@app.errorhandler(405)
def bad_request_error(e):
    template_path = Themes.get_active()
    return render_template(template_path + "/error/error_template.html", status_code=405, error=e), 405

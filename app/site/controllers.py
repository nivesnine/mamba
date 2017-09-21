# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  redirect, url_for, abort
from app.admin.models import Post, Page
from app.auth.models import User
from app.site.models import Themes, PostComment
from app.site.forms import CommentForm
from flask_admin import helpers
import flask_login as login
from app import db

site = Blueprint('site', __name__, url_prefix='')


@site.route('/', methods=['GET'])
def index():
	home = Page.get_home_page()
	if home:
		template_path = Themes.get_active('site')
		return render_template(template_path + "/site/page.html", page=home)
	return redirect(url_for('site.blog'))


@site.route('/blog', defaults={'page': 1}, methods=['GET', 'POST'])
@site.route('/blog/<int:page>', methods=['GET'])
def blog(page):
    posts = Post.get_blog(page)
    template_path = Themes.get_active('site')
    return render_template(template_path + "/site/blog.html", posts=posts)


@site.route('/blog/<slug>', methods=['GET', 'POST'])
def single_post(slug):
    form = CommentForm(request.form)
    if helpers.validate_form_on_submit(form):
        comment = PostComment()
        form.populate_obj(comment)
        comment.writen_by = login.current_user.id
        db.session.add(comment)
        db.session.commit()
    post = Post.get_by_slug(slug)
    if not post:
        abort(404)
    template_path = Themes.get_active('site')
    return render_template(template_path + "/site/single_post.html", post=post, form=form)


@site.route('/<page>', methods=['GET'])
def page(page):
    template_path = Themes.get_active('site')
    page = Page.get_page(page)
    if not page:
        abort(404)
    return render_template(template_path + "/site/page.html", page=page)

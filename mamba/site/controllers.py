# Import flask dependencies
from flask import (
    Blueprint, request, render_template,
    redirect, url_for, abort,
)
from mamba.site.models import PostComment, Post, Page
from mamba.site.forms import CommentForm
from flask_admin import helpers
import flask_login as login
from mamba import db

site = Blueprint('site', __name__, url_prefix='')


@site.route('/', methods=['GET'])
def index():
    home = Page.get_home_page()
    if home:
        return render_template("/site/page.html", page=home)
    return redirect(url_for('site.blog'))


@site.route('/blog', defaults={'page': 1}, methods=['GET', 'POST'])
@site.route('/blog/<int:page>', methods=['GET'])
def blog(page):
    posts = Post.get_blog(page)
    return render_template("/site/blog.html", posts=posts)


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
    return render_template("/site/single_post.html", post=post,
                           form=form)


@site.route('/<page>', methods=['GET'])
def site_page(page):
    page = Page.get_page(page)
    if not page:
        abort(404)
    return render_template("/site/page.html", page=page)

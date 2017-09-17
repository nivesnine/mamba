# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import application, db
from app.admin.models import Post, Page
from app.auth.models import User
from app.site.models import Themes, PostComment
from app.site.forms import CommentForm
from flask_admin import helpers
import flask_login as login
from sqlalchemy import desc

site = Blueprint('site', __name__, url_prefix='')

@site.route('/', methods=['GET'])
def index():
	home = Page.get_home_page()
	if home:
		template_path = Themes.get_active('site')
		return render_template(template_path + "/site/page.html", page=home)
	return redirect(url_for('site.blog'))

@site.route('/blog', defaults={'page': 1}, methods=['GET', 'POST'])
@site.route('/blog/<int:page>', methods=['GET', 'POST'])
def blog(page):
    form = CommentForm(request.form)
    if helpers.validate_form_on_submit(form):
        comment = PostComment()
        form.populate_obj(comment)
        comment.writen_by = login.current_user.id
        db.session.merge(comment)
        db.session.commit()
    per_page = application.config["BLOG_PER_PAGE"]
    posts = Post.query.filter(Post.published==1).order_by(desc('posts_id')).paginate(page, per_page, error_out=False)
    authors = User.all()
    template_path = Themes.get_active('site')
    return render_template(template_path + "/site/blog.html", posts=posts, authors=authors, form=form)

@site.route('/<page>', methods=['GET'])
def page(page):
	template_path = Themes.get_active('site')
	return render_template(template_path + "/site/page.html", page=Page.get_page(page))

# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import application, db
from app.admin.models import Post, Page
from app.auth.models import User
from app.site.models import Themes

site = Blueprint('site', __name__, url_prefix='')

@site.route('/', methods=['GET'])
def index():
	home = Page.get_home_page()
	if home:
		template_path = Themes.get_active('site')
		return render_template(template_path + "/site/page.html", page=home)
	return redirect(url_for('site.blog'))

@site.route('/blog', defaults={'page': 1}, methods=['GET'])
@site.route('/blog/<int:page>', methods=['GET'])
def blog(page):
    per_page = application.config["BLOG_PER_PAGE"]
    posts = Post.query.filter(Post.published==1).order_by('id desc').paginate(page, per_page, error_out=False)
    authors = User.all()
    template_path = Themes.get_active('site')
    return render_template(template_path + "/site/blog.html", posts=posts, authors=authors)

@site.route('/<page>', methods=['GET'])
def page(page):
	template_path = Themes.get_active('site')
	return render_template(template_path + "/site/page.html", page=Page.get_page(page))

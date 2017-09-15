# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.admin.models import Post, Page

site = Blueprint('site', __name__, url_prefix='')

@site.route('/', methods=['GET'])
def index():
	home = Page.get_home_page()
	if home:
		return render_template("site/page.html", page=home)
	return redirect(url_for('site.blog'))

@site.route('/blog', methods=['GET'])
def blog():
    posts = Post.query.filter(Post.published==1).all()
    return render_template("site/blog.html", posts=posts)

@site.route('/<page>', methods=['GET'])
def page(page):
	return render_template("site/page.html", page=Page.get_page(page))

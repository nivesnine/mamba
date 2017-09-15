# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.admin.models import Post

site = Blueprint('site', __name__, url_prefix='')

@site.route('/', methods=['GET'])
def index():
    posts = Post.query.filter(Post.published==1).all()
    return render_template("site/index.html", posts=posts)

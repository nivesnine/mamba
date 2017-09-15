# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.admin.forms import CreatePostForm, EditPostForm
from app.admin.models import Post
from flask_admin import helpers
import flask_login as login
from app import check_login, check_admin

# Create blog blueprint
admin = Blueprint('admin', __name__, url_prefix='/admin')

# Create the blog routes
@admin.route('/blog', methods=['GET'])
@check_login
@check_admin
def blog_list():
    posts = Post.all()
    return render_template("admin/blog/list.html", posts=posts)


@admin.route('/blog/create', methods=['GET', 'POST'])
@check_login
@check_admin
def create_post():
    form = CreatePostForm(request.form)
    if helpers.validate_form_on_submit(form):
        post = Post()
        form.populate_obj(post)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('admin.blog_list'))
    return render_template("admin/blog/post.html", form=form)


@admin.route('/blog/edit/<int:post_id>', methods=['GET', 'POST'])
@check_login
@check_admin
def edit_post(post_id):
    post = Post.query.get(post_id)
    form = EditPostForm(request.form, obj=post)
    if helpers.validate_form_on_submit(form):
        form.populate_obj(post)
        db.session.merge(post)
        db.session.commit()
        return redirect(url_for('admin.blog_list'))
    return render_template("admin/blog/post.html", form=form)

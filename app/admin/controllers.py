# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.admin.forms import CreatePostForm, EditPostForm, CreatePageForm, EditPageForm
from app.admin.models import Post, Page
from flask_admin import helpers
import flask_login as login
from app import check_login, check_admin
import codecs
import translitcodec
import difflib
from datetime import datetime
import re

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

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


# Create the page routes
@admin.route('/page', methods=['GET'])
@check_login
@check_admin
def page_list():
    pages = Page.all()
    return render_template("admin/pages/list.html", pages=pages)


@admin.route('/page/create', methods=['GET', 'POST'])
@check_login
@check_admin
def create_page():
    form = CreatePageForm(request.form)
    if helpers.validate_form_on_submit(form):
        page = Page()
        form.populate_obj(page)
        page.slug = slugify(page.title)
        page.history = "{} created at {}".format(str(login.current_user.email), datetime.now())
        db.session.add(page)
        db.session.commit()
        return redirect(url_for('admin.page_list'))
    return render_template("admin/pages/page.html", form=form)


@admin.route('/page/edit/<int:page_id>', methods=['GET', 'POST'])
@check_login
@check_admin
def edit_page(page_id):
    page = Page.query.get(page_id)
    last_edit = page.html
    form = EditPageForm(request.form, obj=page)
    if helpers.validate_form_on_submit(form):
        form.populate_obj(page)
        page.slug = slugify(page.title)
        page.history = str(login.current_user.email) \
                       + ' updated site at ' \
                       + datetime.now().strftime('%m-%d-%Y %I:%M %p') \
                       + '\n' + _unidiff_output(last_edit, page.html) \
                       + '\n\n' + page.history
        db.session.merge(page)
        db.session.commit()
        return redirect(url_for('admin.page_list'))
    return render_template("admin/pages/page.html", form=form)

def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = codecs.encode(word, 'translit/long')
        if word:
            result.append(word)
    return str(delim.join(result))

def _unidiff_output(expected, actual):
    """
    Helper function. Returns a string containing the unified diff of two multiline strings.
    """
    expected=expected.splitlines(1)
    actual=actual.splitlines(1)

    diff=difflib.unified_diff(expected, actual)

    return ''.join(diff)

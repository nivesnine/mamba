# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  redirect, url_for
from app.auth.forms import LoginForm, RegistrationForm
from app.auth.models import User, Role
from flask_admin.contrib import sqla
from flask_admin import helpers
import flask_login as login
from app import db
from flask_security import SQLAlchemyUserDatastore
from werkzeug.security import generate_password_hash, check_password_hash
from app.site.models import Templates

active_template = Templates.get_active('auth')
template_path = active_template.slug

auth = Blueprint('auth', __name__, url_prefix='/auth')


class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated


@auth.route('/')
def index():
    if not login.current_user.is_authenticated:
        return redirect(url_for('auth.login_view'))
    return redirect(url_for('site.index'))


@auth.route('/login', methods=['GET', 'POST'])
def login_view():
    form = LoginForm(request.form)
    if helpers.validate_form_on_submit(form):
        user = form.get_user()
        login.login_user(user)

    if login.current_user.is_authenticated:
        return redirect(url_for('site.index'))
    return render_template(template_path + '/auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def registration_view():
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):

            user_datastore = SQLAlchemyUserDatastore(db, User, Role)

            email = form.email.data
            encrypted_password = generate_password_hash(form.password.data)

            user_datastore.find_or_create_role(name='end_user', description='End Users')
            user_datastore.create_user(email=email, password=encrypted_password)

            db.session.commit()
            
            user_datastore.add_role_to_user(email, 'end_user')

            db.session.commit()

            user = User.get_user(email)
            login.login_user(user)

            return redirect(url_for('auth.index'))
        return render_template(template_path + '/auth/register.html', form=form)


@auth.route('/logout')
def logout_view():
    login.logout_user()
    return redirect(url_for('auth.index'))

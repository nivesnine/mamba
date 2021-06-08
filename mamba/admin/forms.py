from wtforms import form, fields, validators
from wtforms.widgets import TextArea
from mamba.auth.models import Role, User
from wtforms_alchemy import QuerySelectMultipleField, QuerySelectField
from mamba.site.models import Page, Post

# Blog post creation form
class CreatePostForm(form.Form):
    """
    The form used to create a blog post
    """
    title = fields.StringField('Title', validators=[validators.required()])
    text = fields.StringField('Text', widget=TextArea(), validators=[validators.required()])
    published = fields.BooleanField()
    submit = fields.SubmitField('Submit')


class EditPostForm(CreatePostForm):
    id = fields.HiddenField()


class CreatePageForm(form.Form):
    title = fields.StringField('Title', validators=[validators.required()])
    html = fields.StringField('HTML content', widget=TextArea(), validators=[validators.required()])
    css = fields.StringField('Custom CSS', widget=TextArea())
    js = fields.StringField('Custom JavaScript', widget=TextArea())
    published = fields.BooleanField()
    submit = fields.SubmitField('Submit')
    history = fields.StringField('History', widget=TextArea())


class EditPageForm(CreatePageForm):
    id = fields.HiddenField()


def roles():
    return Role.all()


class CreateUserForm(form.Form):
    display_name = fields.SelectField(
        'Display Name',
        choices=[('alias', 'Alias'), ('first_name', 'First Name'), ('full_name', 'Full Name')]
    )
    email = fields.StringField('Email', validators=[validators.required()])
    password = fields.StringField('Password')

    roles = QuerySelectMultipleField('User Roles', query_factory=roles,
                                     allow_blank=False)

    active = fields.BooleanField()
    submit = fields.SubmitField('Submit')


class EditUserForm(CreateUserForm):
    id = fields.HiddenField()
    roles = QuerySelectMultipleField('User Roles', query_factory=roles,
                                     allow_blank=False)


class CreateRoleForm(form.Form):
    name = fields.StringField('Name', validators=[validators.required()])
    description = fields.StringField('Description', validators=[validators.required()])
    submit = fields.SubmitField('Submit')


class EditRoleForm(CreateRoleForm):
    id = fields.HiddenField()


class EditProfileForm(form.Form):
    first_name = fields.StringField(validators=[validators.length(max=255)])
    last_name = fields.StringField(validators=[validators.length(max=255)])
    alias = fields.StringField(validators=[validators.length(max=255)])
    display_name = fields.SelectField(
        'Display Name',
        choices=[('first_name', 'First Name'), ('full_name', 'Full Name'), ('alias', 'Alias')]
    )
    bio = fields.StringField(validators=[validators.length(max=255)])
    email = fields.StringField(validators=[validators.required(), validators.length(max=120)])
    password = fields.PasswordField(validators=[validators.length(max=255)])
    submit = fields.SubmitField('Submit')


class SettingsForm(form.Form):
    choices = [('blog', 'Blog')]
    try:
        pages = Page.get_published_pages()
        for page in pages:
            choices.append((page.slug, page.title))
    except:
        pass
    site_name = fields.StringField('Site Name', validators=[validators.length(max=255)])
    use_site_logo = fields.BooleanField('Use Logo Instead of Site Name?')
    site_logo_url = fields.StringField('Logo Image Url', validators=[validators.length(max=255)])
    home_page = fields.SelectField(
        'Home Page',
        choices=choices, validators=[validators.required()]
    )
    posts_per_page = fields.IntegerField('Posts per page', validators=[validators.required()])
    blog_sort = fields.SelectField(
        'Blog Sort Direction',
        choices=[('desc', 'Newest Post First'), ('asc', 'Oldest Post First')], validators=[validators.required()]
    )
    submit = fields.SubmitField('Submit')


class MenuForm(form.Form):
    menu = fields.StringField('Menu', widget=TextArea(), validators=[validators.required()])
    submit = fields.SubmitField('Submit')

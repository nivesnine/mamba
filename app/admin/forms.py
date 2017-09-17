from wtforms import form, fields, validators
from wtforms.widgets import TextArea
from app.auth.models import Role
from app.site.models import PostComment
from wtforms_alchemy import QuerySelectMultipleField, ModelForm

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
    display_name = fields.StringField('Display Name', validators=[validators.required()])
    email = fields.StringField('Email', validators=[validators.required()])
    password = fields.StringField('Password')

    roles = QuerySelectMultipleField('User Roles', query_factory=roles,
                                allow_blank=False)
    
    active = fields.BooleanField()
    submit = fields.SubmitField('Submit')

class EditUserForm(CreateUserForm):
    id = fields.HiddenField()

class CreateRoleForm(form.Form):
    name = fields.StringField('Name', validators=[validators.required()])
    description = fields.StringField('Description', validators=[validators.required()])
    submit = fields.SubmitField('Submit')

class EditRoleForm(CreateRoleForm):
    id = fields.HiddenField()

class CreateCommentForm(form.Form):
    comment = fields.StringField('comment', widget=TextArea(), validators=[validators.required()])
    published = fields.BooleanField()
    post = fields.StringField()
    writen_by = fields.StringField()
    submit = fields.SubmitField('Submit')

class EditCommentForm(CreateCommentForm):
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
    
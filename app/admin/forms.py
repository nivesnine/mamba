from wtforms import form, fields, validators
from wtforms.widgets import TextArea
from app.auth.models import Role
from wtforms_alchemy import QuerySelectMultipleField

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

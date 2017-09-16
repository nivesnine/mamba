from wtforms import form, fields, validators
from wtforms.widgets import TextArea

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
    html = fields.StringField('Text', widget=TextArea(), validators=[validators.required()])
    published = fields.BooleanField()
    submit = fields.SubmitField('Submit')
    history = fields.StringField('History', widget=TextArea())

class EditPageForm(CreatePageForm):
	id = fields.HiddenField()

class CreateUserForm(form.Form):
    username = fields.StringField('Username', validators=[validators.required()])
    email = fields.StringField('Email', validators=[validators.required()])
    password = fields.StringField('Password')
    active = fields.BooleanField()
    submit = fields.SubmitField('Submit')

class EditUserForm(CreateUserForm):
    id = fields.HiddenField()

class CreateRoleForm(form.Form):
    name = fields.StringField('Username', validators=[validators.required()])
    description = fields.StringField('Email', validators=[validators.required()])
    submit = fields.SubmitField('Submit')

class EditRoleForm(CreateUserForm):
    id = fields.HiddenField()

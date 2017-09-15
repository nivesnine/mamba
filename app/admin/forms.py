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
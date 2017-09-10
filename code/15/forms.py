from wtforms import Form, fields
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SiteForm(Form):
    base_url = fields.StringField()

class LoginForm(Form):
    username = fields.StringField('Username')
    password = fields.PasswordField('Password')

class NewItem(Form):
    item = fields.StringField(label='Item')
    starting = fields.SubmitField(label='Starting')
    ending = fields.SubmitField(label='Ending')
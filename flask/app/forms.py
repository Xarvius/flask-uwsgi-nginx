from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class LoginForms(FlaskForm):
   username = StringField('Username', validators=[validators.Length(min=4, max=25)])
   submit = SubmitField('Sign In')
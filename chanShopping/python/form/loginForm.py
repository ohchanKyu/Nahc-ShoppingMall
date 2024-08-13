from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField


class LoginForm(FlaskForm):
    id = StringField(label="Input Your Id")
    password = PasswordField(label="Input your password")
    
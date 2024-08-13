from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField


class RegisterForm(FlaskForm):
    name = StringField(label="Input your name")
    email = StringField(label="Input your email")
    email_check = StringField(label="Input Authentic Number")
    id = StringField(label="Input your ID")
    password = PasswordField(label="Input your Password")
    password_check = PasswordField(label="Check Password")

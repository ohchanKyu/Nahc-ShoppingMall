from flask_wtf import FlaskForm
from wtforms import StringField


class FindIdForm(FlaskForm):
    name = StringField(label="가입한 계정의 이름을 입력해주세요")
    email = StringField(label="가입한 계정의 이메일을 입력해주세요")

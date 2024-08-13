from flask_wtf import FlaskForm
from wtforms import StringField


class FindPassForm(FlaskForm):
    email = StringField(label="가입한 계정의 이메일을 입력해주세요.")
    email_check = StringField(label="인증번호를 입력해주세요.")
    id = StringField(label="가입한 계정의 아이디를 입력해주세요.")

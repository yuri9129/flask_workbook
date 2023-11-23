from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):

    username = StringField(
        "ユーザー名",
        validators=[
            DataRequired("ユーザー名は必須です"),
            Length(1, 30, "30文字以内で入力してください")
        ],
    )
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired("メールアドレスは必須です"),
            Email("メールアドレスの形式で入力してください")
        ],
    )
    password = PasswordField(
        "パスワード",
        validators=[
            DataRequired("パスワードは必須です"),
            Length(min=8, max=32)
        ],
    )
    submit = SubmitField("新規登録")


class LoginForm(FlaskForm):
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired("メールアドレスは必須です"),
            Email("メールアドレスの形式で入力してください")
        ],
    )
    password = PasswordField(
        "パスワード",
        validators=[
            DataRequired("パスワードは必須です"),
        ],
    )

    submit = SubmitField("ログイン")
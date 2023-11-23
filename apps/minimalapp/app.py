from email_validator import validate_email, EmailNotValidError
from flask import Flask, render_template, url_for, request, redirect, flash, make_response, session
from flask_debugtoolbar import DebugToolbarExtension
import logging
import os

from flask_mail import Mail, Message

# Flaskクラスをインスタンス化
app = Flask(__name__)
app.config["SECRET_KEY"] = "SeCrEtKeY"

# ログレベルを設定
app.logger.setLevel(logging.DEBUG)

# デバッグツールバーを有効化
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)

# Mailクラスのコンフィグを設定
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
mail = Mail(app)

@app.route("/contact")
def contact():
    response = make_response(render_template("contact.html"))

    response.set_cookie("mykey", "myvalue")
    session["username"] = "myusername"
    return response


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":

        # フォームからの入力値を取得
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True
        if not username:
            flash("ユーザ名を入力してください")
            is_valid = False

        if not email:
            flash("メールアドレスを入力してください")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError as e:
            flash("メールアドレスの形式が正しくありません")
            is_valid = False

        if not description:
            flash("お問い合わせ内容を入力してください")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))


        # メールの送信
        send_email(
            email,
            "お問い合わせありがとうございます",
            "contact_mail",
            username=username,
            description=description,
        )

        # 完了画面へリダイレクト
        flash("お問い合わせありがとうございました")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


@app.route("/")
def index():
    return "Hello World!"


@app.route("/hello/<name>", methods=["GET"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello , {name}!"


@app.get("/hello2")
@app.post("/hello2")
def hello2():
    return "Hello Flask2!"


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


def send_email(to, subject, template, **kwargs):
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)



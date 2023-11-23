from apps.app import db
from apps.crud.models import User
from apps.crud.forms import UserForm
from flask import Blueprint, render_template,redirect, url_for
from flask_login import login_required

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@crud.route("/")
@login_required
def index():
    return render_template("crud/index.html")


# ユーザーの新規作成画面
@crud.route("/user/new", methods=["GET", "POST"])
@login_required
def create_user():
    form = UserForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("crud.users"))

    return render_template("crud/create.html", form=form)


# ユーザーの一覧画面
@crud.route("/users")
@login_required
def users():
    users = User.query.all()
    return render_template("crud/index.html", users=users)


# ユーザー編集画面
@crud.route("/user/<int:user_id>/edit", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    form = UserForm()
    user = User.query.get(user_id)
    if(form.validate_on_submit()):
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))

    return render_template("crud/edit.html", user=user, form=form)


@crud.route("/user<int:user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))

@crud.route("/sql")
@login_required
def sql():
    # db.session.query(User).all()
    # db.session.query(User).first()
    # user = User(
    #     username="myname2",
    #     email="my2@example.com",
    #     password="MyPassW0rd"
    # )
    # db.session.add(user)
    # db.session.commit()
    # db.session.query(User).paginate(1, 1, False)
    # db.session.query(User).filter_by(id=2, username="myname").all()
    # db.session.query(User).filter(User.id == 2, User.username == "myname").all()
    # user = db.session.query(User).filter_by(id=2).first()
    # user.username = "myname modified"
    # db.session.add(user)
    # db.session.commit()
    db.session.query(User).filter_by(id=2).delete()
    db.session.commit()
    return "コンソールログを確認してください"



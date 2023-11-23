from apps.app import db
from apps.crud.models import User
from apps.crud.forms import UserForm
from flask import Blueprint, render_template,redirect, url_for


crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@crud.route("/")
def index():
    return render_template("crud/index.html")


@crud.route("/user/new", methods=["GET", "POST"])
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




@crud.route("/sql")
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



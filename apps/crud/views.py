from apps.app import db
from apps.crud.models import User
from flask import Blueprint, render_template


crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@crud.route("/")
def index():
    return render_template("crud/index.html")

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



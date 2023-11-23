from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from apps.config import config

# SQLAlchemy
db = SQLAlchemy()

# CSRF
csrf = CSRFProtect()

# LoginManager
login_manager = LoginManager()
# 未ログイン時のエンドポイントを指定
login_manager.login_view = "auth.signup"
# ログイン後に表示するメッセージ
login_manager.login_message = ""

def create_app(config_key):
    app = Flask(__name__)

    app.config.from_object(config[config_key])

    # SQLAlchemyとアプリの連携
    db.init_app(app)
    # Migrateとアプリの連携
    Migrate(app, db)
    # CSRFとアプリの連携
    csrf.init_app(app)
    # LoginManagerとアプリの連携
    login_manager.init_app(app)

    toolbar = DebugToolbarExtension(app)

    # crudパッケージ
    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # authパッケージ
    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app


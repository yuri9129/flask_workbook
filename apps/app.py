from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY="MySecretKey",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
    )

    app.config.from_mapping(
        WTF_SCRF_SECRET_KEY="MySecretKey",
    )
    # SQLAlchemyとアプリの連携
    db.init_app(app)
    # Migrateとアプリの連携
    Migrate(app, db)
    # CSRFとアプリの連携
    csrf.init_app(app)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    return app


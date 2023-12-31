from pathlib import Path

basedir = Path(__file__).parent

class BaseConfig:
    SECRET_KEY = 'MySecretKey'
    WTF_CSRF_SECRET_KEY = 'MySecretKey'
    DEBUG_TB_ENABLED = False

class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}

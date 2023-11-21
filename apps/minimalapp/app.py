from flask import Flask

# Flaskクラスをインスタンス化
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"

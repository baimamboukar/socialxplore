from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "The beautiful world of Python"
from flask import Flask

from .joker import get_joke


flask_app = Flask(__name__)


@flask_app.route('/')
def tell_a_joke():
    return get_joke()

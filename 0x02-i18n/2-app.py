#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration proprieties for Babel intance"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
port = 5000

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Renders 1-index.html """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=por)

#!/usr/bin/env python3

"""" Setting up a basic flask App"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """configure languages available"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    determines the best match with our supported language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """renders index.html"""
    return render_temaplate('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)

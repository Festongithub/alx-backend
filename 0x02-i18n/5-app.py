#!/usr/bin/env python3

"""" Setting up a basic flask App"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union


app = Flask(__name__, template_folder='templates')
bable = Babel(app)



class Config:
    """configure languages available"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """
    Get users from session per variable
    """
    try:
        login_as = request.args.get('login_as', None)
        user = users[int(login_as)]
    except Exception:
        user None


@app.before_request
def before_request():
    """
    Operations before requests
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    determines the best match with our supported language
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """renders index.html"""
    return render_temaplate('3-index.html',
                            home_title=_('home_title'),
                            home_header=_('home_header'))


if __name__ == '__main__':
    app.run(debug=True)

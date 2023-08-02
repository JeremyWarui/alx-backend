#!/usr/bin/env python3
"""
Basic Flask app - main file
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
"""instanciate Babel object"""
babel = Babel(app)

"""mock a database users table"""
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """config class that has languages class attribute"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


"""use class Config for flask app"""
app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def home():
    """render home page"""
    return render_template("6-index.html")


@babel.localeselector
def get_locale():
    """getlocale function that returns best match of the languages"""
    locale = request.args.get("locale")
    languages = app.config["LANGUAGES"]
    if locale in languages:
        return locale
    user = int(requests.args.get("login_as"))
    if user:
        local_language = g.user.get("locale")
        if local_language in languages:
            return local_language
    req_language = request.headers.get("locale")
    if req_language in languages:
        return req_language
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """returns user's dict if ID can be found"""
    try:
        user = int(request.args.get("login_as"))
        return users[user]
    except Exception:
        return None


@app.before_request
def before_request():
    """find a user if any, and set it as a global"""
    g.user = get_user()


if __name__ == "__main__":
    app.run()

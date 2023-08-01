#!/usr/bin/env python3
"""
Basic Flask app - main file
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
"""instanciate Babel object"""
babel = Babel(app)


class Config(object):
    """config class that has languages class attribute"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# use class Config for flask app
app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def home():
    """render home page"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """determine best match for supported languages"""
    if request.args.get('locale'):
        locale = request.args.get("locale")
        if locale in app.config["LANGUAGES"]:
            return locale
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run()

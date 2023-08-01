#!/usr/bin/env python3
"""
Basic Flask app - main file
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
"""instanciate Babel object"""
babel = Babel(app)


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
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()

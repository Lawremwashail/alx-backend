#!/usr/bin/env python3
"""
Locale request
"""

from flask import Flask, render_templates, request
from flask_babel import Babel


class Config:
    """
    Config class
    """

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_oject(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Retreives the locale for a webpage and returns the best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Returns default page
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()

# coding=utf-8

from flask import Flask

from cos.ext import mako, init_db

import cos.views.index
import cos.views.menu


def create_app():
    """Create the app instance."""
    app = Flask(__name__, template_folder="templates")
    app.config.from_pyfile("app.cfg")

    # initialize extensions
    mako.init_app(app)

    # mount blueprints
    app.register_blueprint(cos.views.index.bp)
    app.register_blueprint(cos.views.menu.bp)

    print 'create_app'

    return app

app = create_app()
db = init_db(app)

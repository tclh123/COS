# coding=utf-8

from flask import Flask

from cos.models.user import User
from cos.ext import mako, db, login_manager

import cos.views.auth
import cos.views.index
import cos.views.menu


def create_app():
    """Create the app instance."""
    app = Flask(__name__, template_folder="templates")
    app.config.from_pyfile("app.cfg")

    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    # initialize extensions
    mako.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # mount blueprints
    app.register_blueprint(cos.views.index.bp)
    app.register_blueprint(cos.views.menu.bp)
    app.register_blueprint(cos.views.auth.bp)

    return app


@login_manager.user_loader
def load_user(user_id):
    """provide a user_loader callback for Flask-Login
    It should take the unicode ID of a user,
    and return the corresponding user object."""
    return User.query.get(int(user_id))


# @login_manager.token_loader
# def load_token(token):
#     try:
#         max_age = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
#         user_id, hash_a = login_serializer.loads(token, max_age=max_age)
#     except BadData:
#         return None
#     user = User.query.get(user_id)
#     if user is not None:
#         hash_a = hash_a.encode('utf-8')
#         hash_b = sha1(user.password).hexdigest()
#         if constant_time_compare(hash_a, hash_b):
#             return user
#     return None


app = create_app()

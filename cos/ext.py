# coding=utf-8

from flask.ext.mako import MakoTemplates
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

mako = MakoTemplates()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

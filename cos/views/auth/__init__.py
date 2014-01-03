# coding=utf-8

from flask.blueprints import Blueprint


bp = Blueprint("auth", __name__, url_prefix="/auth")

from . import (login, logout)

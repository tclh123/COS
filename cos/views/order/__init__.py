# coding=utf-8

from flask.blueprints import Blueprint


bp = Blueprint("order", __name__, url_prefix="/order")

from . import (user_cart, )

# coding=utf-8

from flask.blueprints import Blueprint
from flask.ext.mako import render_template


bp = Blueprint("index", __name__)


@bp.route('/')
def index():
    return render_template('index.plim')

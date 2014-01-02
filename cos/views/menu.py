# coding=utf-8

from flask import request
from flask.blueprints import Blueprint
from flask.ext.mako import render_template


bp = Blueprint("menu", __name__, url_prefix="/menu")


@bp.route('/', methods=['GET', 'POST'])
def menu():
    return render_template('index.plim')

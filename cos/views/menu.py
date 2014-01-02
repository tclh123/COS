# coding=utf-8

from flask import request
from flask.blueprints import Blueprint
from flask.ext.mako import render_template

from cos.models.menu import Menu

bp = Blueprint("menu", __name__, url_prefix="/menu")


@bp.route('/', methods=['GET', 'POST'])
def menu():
    menus = Menu.query.all()
    return render_template('menu.plim', **locals())

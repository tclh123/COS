# coding=utf-8

from flask import request, redirect, url_for
from flask.blueprints import Blueprint
from flask.ext.mako import render_template
from flask.ext.login import current_user, login_required

from cos.models.menu import Menu
from cos.models.user_cart import UserCart
# from cos.utils.auth import require, HasPermissions

bp = Blueprint("menu", __name__, url_prefix="/menu")


@bp.route('/', methods=['GET', 'POST'])
def menu():
    menus = Menu.query.all()
    return render_template('menu.plim', **locals())


@bp.route('/buy', methods=['GET', 'POST'])
@login_required
def buy():
    meal_id = request.args.get('meal_id')
    menu_id = request.args.get('menu_id')
    if meal_id and menu_id:
        UserCart(user_id=current_user.id,
                 meal_id=meal_id, menu_id=menu_id).commit()
        return redirect(url_for('order.user_cart'))
    return render_template('menu.plim', **locals())

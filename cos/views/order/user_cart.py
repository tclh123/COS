# coding=utf-8

from flask import request, redirect, url_for
from flask.ext.login import current_user, login_required
from flask.ext.mako import render_template

from cos.models.user_cart import UserCart
from . import bp


@bp.route('/user_cart', methods=['GET', 'POST'])
@login_required
def user_cart():
    carts = UserCart.query.filter_by(user_id=current_user.id).all()
    return render_template('user_cart.plim', **locals())

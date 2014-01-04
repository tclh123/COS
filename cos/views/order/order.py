# coding=utf-8

from flask import request, redirect, url_for
from flask.ext.login import current_user, login_required
from flask.ext.mako import render_template

from cos.models.order import Order
from . import bp


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('order.plim', **locals())


# TODO: use url args
@bp.route('/order_form', methods=['GET', 'POST'])
@login_required
def order_form():
    user = current_user
    if request.method == 'POST':
        order_id = request.form.get('order_id')
        if order_id:
            return redirect(url_for('order.index'))
    order_id = request.args.get('order_id')
    if order_id:
        return render_template('order_form.plim', **locals())
    return redirect(url_for('order.index'))

# coding=utf-8

from flask import request, redirect, url_for
from flask.ext.login import login_user, current_user
from flask.ext.mako import render_template

from cos.models.user import User
from . import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('index.index'))
    if request.method == 'POST':
        open_id_kind = request.form.get('open_id_kind', type=int)
        open_id = request.form.get('open_id', type=int)
        user = User.query.filter_by(open_id_kind=open_id_kind,
                                    open_id=open_id).first()
        if user:
            if login_user(user, remember=True):  # TODO: auth_token
                return redirect(request.args.get('next')
                                or url_for('index.index'))
            else:
                errs = 'This username is disabled!'
        else:
            errs = 'Wrong username or password!'

    return render_template('auth/login.plim', **locals())

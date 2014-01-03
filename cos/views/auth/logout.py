# coding=utf-8

from flask import redirect, url_for
from flask.ext.login import logout_user, login_required

from . import bp


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.index'))

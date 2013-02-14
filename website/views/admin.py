# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Blueprint, render_template, url_for, redirect, request
from flask.ext.security import login_required, roles_required
from ..model import Reservation
from ..extensions import db


app = Blueprint('admin', __name__)


@app.route('/')
@login_required
def index():
    return render_template('admin/index.html', items=Reservation.query.all())


@app.route('/delete', methods=('POST',))
@roles_required('admin')
def delete():
    reservation_id = request.values.get('id', None)
    reservation = Reservation.query.filter_by(id=reservation_id).first()
    if reservation is not None:
        db.session.delete(reservation)
        db.session.commit()
    return redirect(url_for('admin.index'))

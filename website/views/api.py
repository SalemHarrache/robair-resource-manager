# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Blueprint, jsonify, request
from ..model import Reservation
from ..utils import is_valid_email

app = Blueprint('api', __name__)


@app.route('/new')
def new():
    jid = request.values.get('jid', None)
    if is_valid_email(jid):
        data = {"error": False}
        data.update(Reservation.new(jid=jid).serialized)
    else:
        data = {"error": True, "error_message": "invalid jid"}
    return jsonify(data)


@app.route('/check')
def check():
    key = request.values.get('key', None)
    if key:
        r = Reservation.query.filter_by(key=key).first()
        if r is not None:
            return jsonify(dict(r.serialized.items() + [("valid", True)]))
    return jsonify(valid=False)

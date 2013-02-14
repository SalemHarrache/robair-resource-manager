# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Blueprint, jsonify, request
from ..model import Reservation

app = Blueprint('api', __name__)


@app.route('/new')
def new():
    data = {"error": False}
    data.update(Reservation.new().serialized)
    return jsonify(data)


@app.route('/check')
def check():
    key = request.values.get('key', None)
    r = Reservation.query.filter_by(key=key).first()
    return jsonify(valid=(r is not None))

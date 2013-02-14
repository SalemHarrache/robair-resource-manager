# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Blueprint
from flask.ext.security import login_required


app = Blueprint('admin', __name__)


@app.route('/')
@login_required
def index():
    return "admin"

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Blueprint


app = Blueprint('api', __name__)


@app.route('/')
def index():
    return "api"

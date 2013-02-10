# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals

from flask import Flask

from .extensions import db


def configured_app(app, config):
    app.config.from_object(config)
    db.init_app(app)
    if app.debug or app.testing:
        @app.errorhandler(400)
        def handle_bad_request_in_debug(exception):
            '''Add a request handler to debug 400 'Bad Request' exceptions.'''
            raise
    return app


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Robair !"

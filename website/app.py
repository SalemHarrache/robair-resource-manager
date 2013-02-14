# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals

import datetime

from flask import Flask
from flask.ext.security import login_required
from .extensions import db, security
from .model import user_datastore


def configured_app(app, config):
    app.config.from_object(config)
    # Setup Flask-SQLAlchemy
    db.init_app(app)
    # Setup Flask-Security
    security.init_app(app, user_datastore)

    # Setup app context
    @app.context_processor
    def inject_date():
        ''' Add context variable. '''
        return dict(now=datetime.datetime.now)
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


@app.route('/admin')
@login_required
def admin():
    return "Hello Admin !"

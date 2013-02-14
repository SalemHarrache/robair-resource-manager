# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import api, admin


DEFAULT_BLUEPRINTS = (
    (api.app, '/api'),
    (admin.app, '/admin')
)


def register_blueprints(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix=url_prefix)


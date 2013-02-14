# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext.security.utils import encrypt_password
from .extensions import db
from .model import user_datastore


def init_users():
    """Initializes users data"""
    # db.create_all()
    user_datastore.create_user(email='admin',
                               password=encrypt_password('admin'))
    db.session.commit()


def init_database(*args, **kwargs):
    init_users()

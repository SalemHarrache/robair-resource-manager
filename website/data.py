# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext.security.utils import encrypt_password
from .extensions import db
from .model import user_datastore


def create_roles():
    user_datastore.create_role(name="admin")
    user_datastore.create_role(name="reader")
    db.session.commit()


def create_users():
    user_datastore.create_user(email="admin", active=True,
                               password=encrypt_password("admin"),
                               roles=['admin'])
    user_datastore.create_user(email="user", active=True,
                               password=encrypt_password("user"),
                               roles=['reader'])
    db.session.commit()


def populate_data(*args, **kwargs):
    create_roles()
    create_users()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext.security.utils import encrypt_password
from .extensions import db
from .model import user_datastore, Reservation


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


def create_reservations():
    Reservation.new('tv@im.quicker.fr', '88d258e-3733-41fa-9e7b-37ab2b85e3df')
    # Reservation.new('tv2@im.quicker.fr', '102746d2-6f18-48fb-b4cf-e1ddff441e9')
    db.session.commit()


def populate_data(*args, **kwargs):
    create_roles()
    create_users()
    create_reservations()

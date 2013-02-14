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
    Reservation.new("88d259c8e-3733-41fa-9e7b-37ab2b85e3df")
    Reservation.new("102746da82-6f18-48fb-b4cf-e1ddff441e9d")
    db.session.commit()


def populate_data(*args, **kwargs):
    create_roles()
    create_users()
    create_reservations()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    def __init__(self, email, password, active=False):
        self.email = email
        self.password = password
        self.active = active

    def __str__(self):
        return '%s %s' % (self.__class__.__name__, self.id)

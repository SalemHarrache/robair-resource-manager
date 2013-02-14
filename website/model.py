# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext.security import UserMixin, RoleMixin, SQLAlchemyUserDatastore
from .extensions import db


# Define models
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime())
    end = db.Column(db.DateTime())
    key = db.Column(db.UnicodeText())


user_datastore = SQLAlchemyUserDatastore(db, User, Role)

__all__ = [Role, User, user_datastore]

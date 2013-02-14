# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import uuid
from flask.ext.security import UserMixin, RoleMixin, SQLAlchemyUserDatastore
from .extensions import db
from .utils import dump_datetime


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
    id = db.Column(db.Integer(), primary_key=True)
    start = db.Column(db.DateTime())
    end = db.Column(db.DateTime())
    key = db.Column(db.UnicodeText())

    @classmethod
    def new(cls, key=None):
        start = datetime.datetime.now()
        end = datetime.datetime.now() + datetime.timedelta(seconds=999999)
        new_item = cls(start=start, end=end, key=key)
        db.session.add(new_item)
        db.session.commit()
        if key is None:
            new_item.key = u"%s%s" % (new_item.id, str(uuid.uuid4()))
            db.session.merge(new_item)
            db.session.commit()
        return new_item

    @property
    def serialized(self):
        '''Return object data in easily serializeable format'''
        return {'id': self.id,
                'start': dump_datetime(self.start),
                'end': dump_datetime(self.end),
                'key': self.key}


user_datastore = SQLAlchemyUserDatastore(db, User, Role)

__all__ = [Role, User, user_datastore]

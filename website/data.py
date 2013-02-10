# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from .extensions import db
from .model import User


def init_users():
    """Initializes users data"""
    db.session.add(User('snake.h@gmail.com', 'snake'))
    db.session.add(User('naomi.h@gmail.com', 'naomi'))
    db.session.commit()

def init_database(*args, **kwargs):
    init_users()

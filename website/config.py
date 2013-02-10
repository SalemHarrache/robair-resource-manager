# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class DevConfig(object):
    '''Dev configuration.'''

    SERVER_PATH = "http://localhost"
    SECRET_KEY = "secret"

    SQLALCHEMY_ECHO = True

    # SQLite Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/robair-portal.db'

    # Server
    DEBUG = True
    TESTING = False
    PORT = 9090
    HOST = "127.0.0.1"


class ProdConfig(DevConfig):
    '''Prod configuration.'''

    SECRET_KEY = "my_super_secret_key"

    SQLALCHEMY_ECHO = False

    # Debug
    DEBUG = False
    TESTING = False

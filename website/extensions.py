# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask_sqlalchemy import SQLAlchemy
from flask.ext.security import Security


db = SQLAlchemy()
security = Security()

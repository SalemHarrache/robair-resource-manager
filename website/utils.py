# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


def is_valid_email(email):
    if email is not None:
        if len(email) > 7:
            regex = "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]"\
                    "{1,3})(\\]?)$"
            if re.match(regex, email):
                return 1
    return 0

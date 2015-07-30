# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""
Application settings.

    Can contain something like this:
        "host": '0.0.0.0',
        "port": 8080,
        "debug": True
"""
app = {
    "debug": False
}

file_system = "direct"
path = ""

"""
LOCAL SETTINGS.

    Allow any settings to be defined in local_settings.py which should be
ignored in your version control system allowing for settings to be
defined per machine.
"""
try:
    from local_settings import *
except ImportError:
    pass

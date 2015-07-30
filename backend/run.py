#!/usr/bin/env python
__author__ = 'boonya'

from app import app
from app import init_app_config

if __name__ == '__main__':
    app.run(**init_app_config)

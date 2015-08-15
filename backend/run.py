#!/usr/bin/env python
__author__ = 'boonya'

from app import create_app
from app import init_app_config

app = create_app()

if __name__ == '__main__':
    config = init_app_config()
    app.run(**config)

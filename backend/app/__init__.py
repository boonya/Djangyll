# -*- coding: utf-8 -*-
__author__ = 'boonya'

from flask import Flask
from flask.ext.cors import cross_origin

app = Flask(__name__)

@app.after_request
@cross_origin(headers=['x-auth-token', 'Content-Type'],
              methods=['PATCH', 'DELETE', 'PUT'])
def after_request(response):
    """Apply CORS for all requests.

    :param response:
    :return:
    """
    return response

from config.common import app as init_app_config
from controllers import post

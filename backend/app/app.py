# -*- coding: utf-8 -*-
__author__ = 'boonya'

import os
from flask import Flask, g
from flask.ext.cors import cross_origin
from .utils.response import Response
from .reasons import errors
from .config import common

# blueprints
from .blueprints.post import post

BASE_DIR = os.path.relpath(os.path.dirname(__file__))

BLUEPRINTS = (
    post,
)


def create_app(app_name='djangyll'):
    """Create pre-configured instance of application.

    :param string app_name:
    :param dict blueprints:
    :return Flask:
    """
    app = Flask(app_name)

    blueprints_fabrics(app, BLUEPRINTS)
    allow_cross_origin(app)
    error_pages(app)
    global_vars(app)

    return app


def blueprints_fabrics(app, blueprints):
    """Configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def init_app_config():
    """Return initial application config.

    :return dict:
    """
    return common.app


def error_pages(app):
    """HTTP error pages definitions."""

    @app.errorhandler(403)
    def forbidden_page(error):
        return Response.failure(errors.FORBIDDEN, 403, error=error)

    @app.errorhandler(404)
    def page_not_found(error):
        return Response.failure(errors.NOT_FOUND, 404, error=error)

    @app.errorhandler(405)
    def method_not_allowed(error):
        return Response.failure(errors.METHOD_NOT_ALLOWED, 405, error=error)

    @app.errorhandler(500)
    def server_error_page(error):
        return Response.failure(errors.SERVER_ERROR, 500, error=error)


def allow_cross_origin(app):
    @app.after_request
    @cross_origin(headers=['x-auth-token', 'Content-Type'],
                  methods=['PATCH', 'DELETE', 'PUT'])
    def after_request(response):
        """Apply CORS for all requests.

        :param response:
        :return:
        """
        return response


def global_vars(app):
    @app.before_request
    def gdebug():
        if app.debug:
            g.debug = True
        else:
            g.debug = False

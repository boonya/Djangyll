# -*- coding: utf-8 -*-
__author__ = 'boonya'
from flask import request


class Request(object):
    """Request wrapper helper."""

    @staticmethod
    def get(key):
        """Returns value associated with passed key.

        :param mixed key:
        :return mixed:
        """
        return request.form.get(key, None)

    @staticmethod
    def dict():
        """Returns request data as dict.

        :return dict:
        """
        return dict(
            (key, request.form.get(key, None)) for key in request.form.keys())

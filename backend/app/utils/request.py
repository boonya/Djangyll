# -*- coding: utf-8 -*-
__author__ = 'boonya'

import json
from flask import request


class Request(object):
    """Request wrapper helper."""

    @staticmethod
    def get(key):
        """Returns value associated with passed key.

        :param mixed key:
        :return mixed:
        """
        if request.data:
            return json.loads(request.data).get(key, None)
        elif request.form.__len__:
            return request.form.get(key, None)
        else:
            return None

    @staticmethod
    def dict():
        """Returns request data as dict.

        :return dict:
        """
        if request.data:
            return json.loads(request.data)
        elif request.form.__len__:
            return dict((key, request.form.get(key, None)) for key in
                        request.form.iterkeys())
        else:
            return {}

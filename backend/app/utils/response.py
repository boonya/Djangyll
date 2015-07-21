# -*- coding: utf-8 -*-
__author__ = 'boonya'
from flask import make_response
import json


class Response(object):

    """Response wrapper helper."""

    @staticmethod
    def success(data, code=200):
        """Returns successful response.

        :param str body:
        :param int code:
        :return ResponseBase:
        """
        response = make_response(data, code)
        response.headers['Content-Type'] = 'application/json'
        return response

    @staticmethod
    def failure(reason, code=400):
        """Returns response with serialized json string about error reason.

        :param str reason:
        :param int code:
        :return ResponseBase:
        """
        response = make_response(json.dumps({"error": reason}), code)
        response.headers['Content-Type'] = 'application/json'
        return response

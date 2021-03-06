# -*- coding: utf-8 -*-
__author__ = 'boonya'

import json
from flask import make_response


class Response(object):
    """Response wrapper helper."""

    @staticmethod
    def success(data, code=200, serializer=None):
        """Returns successful response.

        :param str body:
        :param int code:
        :return ResponseBase:
        """

        if serializer:
            data = json.dumps(data, cls=serializer)
        else:
            data = json.dumps(data)

        response = make_response(data, code)
        response.headers['Content-Type'] = 'application/json'
        return response

    @staticmethod
    def failure(reason, code=400, **kwargs):
        """Returns response with serialized json string about error reason.

        :param str reason:
        :param int code:
        :param kwargs:
        :return ResponseBase:
        """
        response = make_response(json.dumps({"reason": reason}), code)
        response.headers['Content-Type'] = 'application/json'
        return response

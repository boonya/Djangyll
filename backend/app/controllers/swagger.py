# -*- coding: utf-8 -*-
__author__ = 'boonya'

from app import app
from flask import jsonify
from flask_swagger import swagger as flask_swagger
from app.config import swagger


@app.route('/swagger/spec.json', methods=['GET'])
def spec():
    """Returns the swagger spec.

    Read more by this link https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md
    :return:
    """
    swagger_spec = flask_swagger(app)

    for (key, value) in swagger.SPEC.iteritems():
        swagger_spec[key] = value

    return jsonify(swagger_spec)

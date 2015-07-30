# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""
Read more by this link:
https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md
"""

SPEC = dict(
    info={
        "title": "Djangyll App",
        "license": {
            "name": "MIT",
            "url": "https://raw.githubusercontent.com/boonya/Djangyll/master/LICENSE"
        },
        "version": "1.0.1",
        "contact": {
            "name": "Sergii boonya Buinytskyi",
            "url": "http://boonya.info/",
            "email": "support@boonya.info"
        }
    },
    consumes=["application/json"],
    produces=["application/json"],
    tags=[{
        "name": "post",
        "description": "Everything about your Posts"
    }]
)

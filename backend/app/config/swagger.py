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
    }],
    definitions={
        "PostModel": {
            "description": "Post",
            "schema": {
                "type": "object",
                "example": {
                    "id": "2010-10-25-about.markdown",
                    "category": "Uncategorised",
                    "permalink": "/about.html",
                    "layout": "post",
                    "language": "uk-UA",
                    "title": "Про нас",
                    "cat_slug": "uncategorised",
                    "featured": 0,
                    "date": "2010-10-25T19:00:00",
                    "slug": "about",
                    "body": "string"
                }
            }
        }
    }
)

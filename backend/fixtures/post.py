# -*- coding: utf-8 -*-
__author__ = 'boonya'
from app.utils.fs.interface import FileSystemInterface
from datetime import datetime

post_raw = """
---
layout: post
title: "Про нас"
slug: about
date: 2010-10-25 22:00:00.000000000 +03:00
category: Категория
cat_slug: some-category
featured: false
language: uk-UA
permalink: /about.html
---
###Заголовочек
содержимое
"""

post_data = {
    'layout': u'post',
    'title': u'Про нас',
    'slug': u'about',
    'date': datetime(2010, 10, 25, 19, 0, 0, 0),
    'category': u'Категория',
    'cat_slug': u'some-category',
    'featured': False,
    'language': u'uk-UA',
    'permalink': u'/about.html',
    'body': u'###Заголовочек\nсодержимое\n'
}

post_json = '{"category": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", "body": "###\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u0447\u0435\u043a\\n\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435\\n", "permalink": "/about.html", "layout": "post", "language": "uk-UA", "title": "\u041f\u0440\u043e \u043d\u0430\u0441", "cat_slug": "some-category", "id": "post-id", "featured": false, "date": "2010-10-25T19:00:00", "slug": "about"}'


class MockedFs(FileSystemInterface):
    def list(self):
        return []

    def read(self, path):
        return post_raw

    def write(self, path, data):
        return True

    def remove(self, source):
        return True

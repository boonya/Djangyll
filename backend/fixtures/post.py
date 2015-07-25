# -*- coding: utf-8 -*-
__author__ = 'boonya'
from app.utils.fs.interface import FileSystemInterface

post_raw = """
        ---
        layout: post
        title: "Про нас"
        slug: about
        date: 2010-10-25 22:00:00.000000000 +03:00
        category: Some category
        cat_slug: some-category
        featured: false
        language: uk-UA
        permalink: /about.html
        ---
        ###Title of post
        simple text
        """

post_data = {
    'layout': 'post',
    'title': 'Про нас',
    'slug': 'about',
    'date': '2010-10-25 22:00:00.000000000 +03:00',
    'category': 'Some category',
    'cat_slug': 'some-category',
    'featured': False,
    'language': 'uk-UA',
    'permalink': '/about.html',
    'body': """
        ###Title of post
        simple text
    """
}


class MockedFs(FileSystemInterface):
    def list(self):
        return []

    def read(self, path):
        return post_raw

    def write(self, path, data):
        return data

    def remove(self, source):
        return True


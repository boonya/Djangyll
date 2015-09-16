# -*- coding: utf-8 -*-
__author__ = 'boonya'

import re
import yaml
import json
import os.path
from app.utils.fs.interface import FileSystemInterface


def get_post_raw_data(file_name):
    path = os.path.join(os.path.dirname(__file__), file_name)

    with open(path, 'r') as fh:
        data = fh.read()

    return data


def post_decode(yaml_data):
    unicode_fields = ('title', 'body')

    entries = re.split("---\n+", yaml_data)

    data = yaml.load(entries[1])

    data['body'] = entries[2]

    for field in unicode_fields:
        if isinstance(data[field], str):
            data[field] = unicode(data[field], "utf-8")

    return data


post_raw = get_post_raw_data('post.md')

post_data = post_decode(post_raw)

post_data['id'] = "post-id"
post_json = json.dumps(post_data)


class MockedFs(FileSystemInterface):
    def list(self):
        return []

    def read(self, path):
        return post_raw

    def write(self, path, data):
        return True

    def remove(self, source):
        return True

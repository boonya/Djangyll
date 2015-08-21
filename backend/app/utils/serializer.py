# -*- coding: utf-8 -*-
__author__ = 'boonya'

import json


class Serializer(json.JSONEncoder):
    def default(self, obj):
        return super(Serializer, self).default(obj)

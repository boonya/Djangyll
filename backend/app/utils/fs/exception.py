# -*- coding: utf-8 -*-
__author__ = 'boonya'


class NotExistsException(Exception):
    """Special exception for classes which will implement FileSystemInterface."""

    def __init__(self, *args, **kwargs):
        super(NotExistsException, self).__init__(*args, **kwargs)

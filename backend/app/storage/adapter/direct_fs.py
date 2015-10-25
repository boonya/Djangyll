# -*- coding: utf-8 -*-
__author__ = 'boonya'

from os import listdir, remove
from os.path import isfile, join, isdir, exists
# from ...storage import NotExistsException
from . import IStorageAdapter


class DirectFs(IStorageAdapter):
    container = None

    def __init__(self, options):
        """Constructor.

        :param dict options:
        :return:
        """
        if not 'container' in options:
            raise RuntimeError("Illegal configuration for DirectFs adapter.")

        if not isdir(options['container']) or not exists(options['container']):
            raise ValueError("'%s' is not a directory or does not exist." % options['container'])

        self.container = options['container'].rstrip('/')

    def listing(self):
        return [f for f in listdir(self.container) if
                isfile(join(self.container, f))]

    def read(self, path):
        file_path = self.container + '/' + path

        if not exists(file_path) or not isfile(file_path):
            raise NotExistsException("'%s' is unknown file." % path)

        with open(file_path, 'r') as fh:
            data = fh.read()

        return data

    def create(self, path, data):
        file_path = self.container + '/' + path

        with open(file_path, 'w') as fh:
            fh.write(data)

        with open(file_path, 'r') as fh:
            result = fh.read()

        return result

    def delete(self, path):
        file_path = self.container + '/' + path

        if not exists(file_path) or not isfile(file_path):
            raise NotExistsException("'%s' is unknown file." % path)

        remove(file_path)

        return True

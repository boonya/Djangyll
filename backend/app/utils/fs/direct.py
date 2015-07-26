# -*- coding: utf-8 -*-
__author__ = 'boonya'

from os import listdir, remove
from os.path import isfile, join, isdir, exists
from app.utils.fs.interface import FileSystemInterface
from app.utils.fs.exception import NotExistsException


class Direct(FileSystemInterface):
    container = None

    def __init__(self, container):
        """Constructor.

        :param string container:
        :return:
        """
        if not isdir(container) or not exists(container):
            raise ValueError(
                "'%s' is not a directory or does not exist." % container)

        self.container = container.rstrip('/')

    def list(self):
        return [f for f in listdir(self.container) if
                isfile(join(self.container, f))]

    def read(self, path):
        file_path = self.container + '/' + path

        if not exists(file_path) or not isfile(file_path):
            raise NotExistsException("'%s' is unknown file." % path)

        with open(file_path, 'r') as fh:
            data = fh.read()

        return data

    def write(self, path, data):
        file_path = self.container + '/' + path

        with open(file_path, 'w') as fh:
            fh.write(data)

        with open(file_path, 'r') as fh:
            result = fh.read()

        return result

    def remove(self, path):
        file_path = self.container + '/' + path

        if not exists(file_path) or not isfile(file_path):
            raise NotExistsException("'%s' is unknown file." % path)

        remove(file_path)

        return True

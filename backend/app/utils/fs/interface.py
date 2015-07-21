# -*- coding: utf-8 -*-
__author__ = 'boonya'


class FileSystemInterface(object):
    def list(self):
        raise NotImplementedError('List is not implemented yet.')

    def read(self, path):
        raise NotImplementedError('Read is not implemented yet.')

    def write(self, path, data):
        raise NotImplementedError('Write is not implemented yet.')

    def copy(self, source, destination):
        raise NotImplementedError('Copy is not implemented yet.')

    def move(self, source, destination):
        raise NotImplementedError('Move is not implemented yet.')

    def remove(self, source, destination):
        raise NotImplementedError('Remove is not implemented yet.')

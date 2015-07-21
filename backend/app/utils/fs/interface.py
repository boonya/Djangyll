# -*- coding: utf-8 -*-
__author__ = 'boonya'


class FileSystemInterface(object):
    def list(self):
        raise NotImplementedError('Method is not implemented yet.')

    def read(self, path):
        raise NotImplementedError('Method is not implemented yet.')

    def write(self, path, data):
        raise NotImplementedError('Method is not implemented yet.')

    def copy(self, source, destination):
        raise NotImplementedError('Method is not implemented yet.')

    def move(self, source, destination):
        raise NotImplementedError('Method is not implemented yet.')

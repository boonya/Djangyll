# -*- coding: utf-8 -*-
__author__ = 'boonya'


class FileSystemInterface(object):
    def list(self):
        """List of current directory.

        :return list:
        """
        raise NotImplementedError('List is not implemented yet.')

    def read(self, path):
        """Read the file from current directory.

        :param str path:
        :return str:
        """
        raise NotImplementedError('Read is not implemented yet.')

    def write(self, path, data):
        """Write data to file.

        :param str path:
        :param str data:
        :return str:
        """
        raise NotImplementedError('Write is not implemented yet.')

    def remove(self, source):
        """Remove passed file.

        :param str source:
        :return boolean:
        """
        raise NotImplementedError('Remove is not implemented yet.')

    def copy(self, source, destination):
        raise NotImplementedError('Copy is not implemented yet.')

    def move(self, source, destination):
        raise NotImplementedError('Move is not implemented yet.')

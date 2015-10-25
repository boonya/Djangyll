# -*- coding: utf-8 -*-
__author__ = 'boonya'


class IStorageAdapter:
    """@TODO: Need to implement checking for existant methods on start up.
    """

    def listing(self):
        """Return listing of objects.

        :return list:
        """
        raise NotImplementedError("list")

    def read(self, id):
        """Return content of object.

        :param string id:
        :return dict:
        """
        raise NotImplementedError("read")

    def create(self, id, data):
        """Create object.

        :param string id:
        :param dict data:
        :return dict:
        """
        raise NotImplementedError("create")

    def update(self, id, data):
        """Update object.

        :param string id:
        :param dict data:
        :return dict:
        """
        raise NotImplementedError("update")

    def delete(self, id):
        """Delete object.

        :param string id:
        :return bool:
        """
        raise NotImplementedError("delete")

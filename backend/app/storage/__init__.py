# -*- coding: utf-8 -*-
__author__ = 'boonya'


from ..config import common as common_config
from .adapter.direct_fs import DirectFs


class Storage:
    adapter = None

    def __init__(self):
        """Simple Constructor.

        :param fs_adapter:
        :return:
        """
        # @TODO: Need to rewrite this dirty hack!
        site_config = common_config.sites['boonya']

        if 'direct' == site_config['fs']:
            self.adapter = DirectFs(site_config['path'])

        if not self.adapter:
            raise RuntimeError("Illegal storage adapter.")

    def listing(self):
        """Return listing of objects.

        :return list:
        """
        self.adapter.listing()

    def read(self, id):
        """Return content of object.

        :param string id:
        :return dict:
        """
        self.adapter.read(id)

    def create(self, id, data):
        """Create object.

        :param string id:
        :param dict data:
        :return dict:
        """
        self.adapter.create(id, data)

    def update(self, id, data):
        """Update object.

        :param string id:
        :param dict data:
        :return dict:
        """
        self.adapter.update(id, data)

    def delete(self, id):
        """Delete object.

        :param string id:
        :return bool:
        """
        self.adapter.delete(id)


class NotExistsException(Exception):
    def __init__(self, *args, **kwargs):
        super(NotExistsException, self).__init__(*args, **kwargs)

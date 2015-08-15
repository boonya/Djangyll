# -*- coding: utf-8 -*-
__author__ = 'boonya'

from .direct import Direct
from ...config import common as common_config


class Fs(object):
    """File system chooser."""

    @staticmethod
    def get():
        fs = None

        # @TODO: Need to rewrite this dirty hack!
        site_config = common_config.sites['boonya']

        if 'direct' == site_config['fs']:
            fs = Direct(site_config['path'])

        if not fs:
            raise RuntimeError("File system was not chosen.")

        return fs

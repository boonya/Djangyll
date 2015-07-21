# -*- coding: utf-8 -*-
__author__ = 'boonya'
from app.utils.fs.direct import Direct
from app.config import common as config


class Fs(object):
    """File system chooser."""

    @staticmethod
    def get():
        fs = None

        if 'direct' == config.file_system:
            fs = Direct(config.path)

        if not fs:
            raise RuntimeError("File system was not chosen.")

        return fs

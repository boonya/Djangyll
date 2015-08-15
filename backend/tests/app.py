# -*- coding: utf-8 -*-
__author__ = 'boonya'

import unittest
import logging
import sys


def create_app():
    # from tests.controllers.post import CtrlPostTestCase
    # from tests.models.post import PostTestCase
    # from tests.models.post import PostModelTestCase
    # from tests.models.post import PostSerializerTestCase
    # from tests.utils.fs.direct import DirectTestCase
    return TestApp


class TestApp:
    def __init__(self):
        logging.basicConfig(stream=sys.stderr)

    @staticmethod
    def run():
        unittest.main()

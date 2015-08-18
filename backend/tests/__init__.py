# -*- coding: utf-8 -*-
__author__ = 'boonya'

import unittest
from .controllers.post import CtrlPostTestCase
from .models.post import PostTestCase, PostModelTestCase, \
    PostSerializerTestCase
from .utils.fs.direct import DirectTestCase


class TestRunner(object):
    runner = None

    def create_app(self):
        self.runner = unittest.TextTestRunner(verbosity=2)
        self._create_suite()
        return self

    def run(self):
        self.runner.run(self.suite)

    def _create_suite(self):
        loader = unittest.TestLoader()

        test_cases = [DirectTestCase, PostTestCase, PostModelTestCase,
                      PostSerializerTestCase]

        suite = []
        for case in test_cases:
            suite.append(loader.loadTestsFromTestCase(case))

        self.suite = unittest.TestSuite(suite)

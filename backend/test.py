#!/usr/bin/env python
__author__ = 'boonya'

from tests import TestRunner

if __name__ == '__main__':
    test_app = TestRunner().create_app()
    test_app.run()

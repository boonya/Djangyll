#!/usr/bin/env python
__author__ = 'boonya'
import unittest
import logging
import sys

from tests.controllers.post import CtrlPostTestCase
from tests.models.post import ModelPostTestCase

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    unittest.main()

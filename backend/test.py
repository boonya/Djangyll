#!/usr/bin/env python
__author__ = 'boonya'
import unittest
import logging
import sys

from tests.controllers.post import CtrlPostTestCase
from tests.models.post import PostTestCase
from tests.models.post import PostModelTestCase
from tests.models.post import PostSerializerTestCase
#from tests.utils.fs.direct import DirectTestCase

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    unittest.main()

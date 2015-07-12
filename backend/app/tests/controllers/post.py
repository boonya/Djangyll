# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""Test cases for post controller."""

from app import app
import unittest
import mock
import json


class TestCase(unittest.TestCase):
    client = app.test_client()

    def test_listing(self):
        result = self.client.get('/post')

        self.assertEqual(result.status_code, 200)
        self.assertIsInstance(json.loads(result.data), list)

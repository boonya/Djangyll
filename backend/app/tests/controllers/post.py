# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""Test cases for post controller."""

from app import app
import unittest
import mock
import json


class CtrlPostTestCase(unittest.TestCase):
    """Test cases for PostView."""

    client = app.test_client()

    def setUp(self):
        """Start patching objects."""
        self.patcher_fs = mock.patch('app.controllers.post.Fs')
        self.patcher_post = mock.patch('app.controllers.post.Post')
        self.mocked_fs = self.patcher_fs.start()
        self.mocked_post = self.patcher_post.start()
        self.mocked_fs.get.return_value = None
        self.mocked_post.return_value = MockedPost()

    def tearDown(self):
        """Stop patching objects."""
        self.patcher_fs.stop()
        self.patcher_post.stop()

    def test_listing(self):
        response = self.client.get('/post')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_get(self):
        response = self.client.get('/post/some-post.md')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)

    def test_create(self):
        response = self.client.post('/post', data={})

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)

    def test_update(self):
        response = self.client.put('/post/some-post.md')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)

    def test_delete(self):
        response = self.client.delete('/post/some-post.md')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)

    def test_bulk_update(self):
        self.skipTest("'test_bulk_update' is not implemented yet.")

    def test_bulk_delete(self):
        self.skipTest("'test_bulk_delete' is not implemented yet.")


class MockedPost(object):
    def list(self):
        return []

    def read(self, *args):
        return {}

    def save(self, *args):
        return {}

    def update(self, *args):
        return {}

    def delete(self, *args):
        return {}

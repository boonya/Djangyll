# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""Test cases for post controller."""

from app import create_app
import unittest
import mock
import json


class PostApiTestCase(unittest.TestCase):
    """Test cases for PostView."""

    client = create_app().test_client()

    def setUp(self):
        """Start patching objects."""
        self.patcher_fs = mock.patch('app.blueprints.post.view.Fs')
        self.patcher_post = mock.patch('app.blueprints.post.view.Post')
        self.mocked_fs = self.patcher_fs.start()
        self.mocked_post = self.patcher_post.start()
        self.mocked_fs.get.return_value = None
        self.mocked_post.return_value = MockedPost()

    def tearDown(self):
        """Stop patching objects."""
        self.patcher_fs.stop()
        self.patcher_post.stop()

    def test_listing(self):
        response = self.client.get('/post/')

        self._assertionDict(response, u'[]')

    def test_get(self):
        response = self.client.get('/post/some-post.md')

        self._assertionDict(response, u'{"id": "some-post.md"}')

    def test_create(self):
        response = self.client.post('/post/', data={})

        self._assertionDict(response, u'{}')

    def test_update(self):
        response = self.client.put('/post/some-post.md', data={})

        self._assertionDict(response, u'{"id": "some-post.md"}')

    def test_delete(self):
        response = self.client.delete('/post/some-post.md')

        self._assertionDict(response, u'{"success": true}')

    def test_bulk_update(self):
        self.skipTest("'test_bulk_update' is not implemented yet.")

    def test_bulk_delete(self):
        self.skipTest("'test_bulk_delete' is not implemented yet.")

    def _assertionDict(self, response, expected_data):
        self.assertEqual(response.status_code, 200)

        encoded_data = json.loads(response.data)

        self.assertIsInstance(encoded_data, unicode)
        self.assertEqual(encoded_data, expected_data)


class MockedPost(object):
    def list(self):
        return []

    def read(self, post_id):
        return {'id': post_id}

    def save(self, *args):
        return {}

    def update(self, post_id, *args):
        return {'id': post_id}

    def delete(self, *args):
        return {'success': True}

# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""Test cases for post controller."""

from app import create_app
import unittest
import mock
from app.utils.fs.exception import NotExistsException


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

        mocked_post = self.mocked_post()

        mocked_post.list.return_value = []
        mocked_post.read.return_value = {'id': 'some-post.md'}
        mocked_post.save.return_value = {'id': 'some-post.md'}
        mocked_post.update.return_value = {'id': 'some-post.md'}
        mocked_post.delete.return_value = {'success': True}

    def tearDown(self):
        """Stop patching objects."""
        self.patcher_fs.stop()
        self.patcher_post.stop()

    def test_listing(self):
        response = self.client.get('/post/')

        self._compare_assertions(response, 200, '[]')

    def test_get(self):
        response = self.client.get('/post/some-post.md')

        self._compare_assertions(response, 200, '{"id": "some-post.md"}')

    def test_get_404(self):
        self.mocked_post().read.side_effect = NotExistsException('foo')

        response = self.client.get('/post/unknown-post.md')

        self._compare_assertions(response, 404,
                                 '{"error": "does_not_exist"}')

    def test_create(self):
        response = self.client.post('/post/', data={})

        self._compare_assertions(response, 200, '{"id": "some-post.md"}')

    def test_update(self):
        response = self.client.put('/post/some-post.md', data={})

        self._compare_assertions(response, 200, '{"id": "some-post.md"}')

    def test_delete(self):
        response = self.client.delete('/post/some-post.md')

        self._compare_assertions(response, 200, '{"success": true}')

    def test_bulk_update(self):
        self.skipTest("'test_bulk_update' is not implemented yet.")

    def test_bulk_delete(self):
        self.skipTest("'test_bulk_delete' is not implemented yet.")

    def _compare_assertions(self, response, expected_code, expected_data):
        self.assertEqual(response.status_code, expected_code)

        self.assertIsInstance(response.data, str)
        self.assertEqual(response.data, expected_data)

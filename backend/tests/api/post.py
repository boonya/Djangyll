# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""Test cases for post controller."""

from app import create_app
import unittest
import mock
import json
from app.blueprints.post.post import PostModel
from app.utils.fs.exception import NotExistsException


class PostApiTestCase(unittest.TestCase):
    """Test cases for PostView."""

    client = create_app().test_client()

    error_404_response = '{"reason": "not_found"}'

    mocked_post_data = {'id': 'some-post.md'}

    patchable = {'fs': 'app.blueprints.post.view.Fs',
                 'post': 'app.blueprints.post.view.Post',
                 'serializer': 'app.blueprints.post.view.PostSerializer'
                 }

    def setUp(self):
        """Start patching objects."""
        self.patcher = self.mocked = {}

        for name, path in self.patchable.iteritems():
            self.patcher[name] = mock.patch(path)
            self.mocked[name] = self.patcher[name].start()

        self.mocked['fs'].get.return_value = None

        mocked_post = self.mocked['post']()
        mocked_post.list.return_value = []
        mocked_post.delete.return_value = {'success': True}
        mocked_post.read.return_value =\
            mocked_post.save.return_value =\
            mocked_post.update.return_value =\
            PostModel(**self.mocked_post_data)

        mocked_serializer = self.mocked['serializer']()
        mocked_serializer.encode.return_value = json.dumps(
            self.mocked_post_data)

    def tearDown(self):
        """Stop patching objects."""
        for name in self.patcher.iterkeys():
            self.patcher[name].stop()

    def test_listing(self):
        response = self.client.get('/post/')

        self._compare_assertions(response, 200, '[]')

    def test_get(self):
        response = self.client.get('/post/some-post.md')

        self._compare_assertions(response, 200,
                                 json.dumps(self.mocked_post_data))

    def test_get_404(self):
        self.mocked['post']().read.side_effect = NotExistsException('foo')

        response = self.client.get('/post/unknown-post.md')

        self._compare_assertions(response, 404, self.error_404_response)

    def test_create(self):
        response = self.client.post('/post/', data={})

        self._compare_assertions(response, 200,
                                 json.dumps(self.mocked_post_data))

    def test_update(self):
        response = self.client.put('/post/some-post.md', data={})

        self._compare_assertions(response, 200,
                                 json.dumps(self.mocked_post_data))

    def test_update_404(self):
        self.mocked['post']().update.side_effect = NotExistsException('foo')

        response = self.client.put('/post/unknown-post.md', data={})

        self._compare_assertions(response, 404, self.error_404_response)

    def test_delete(self):
        response = self.client.delete('/post/some-post.md')

        self._compare_assertions(response, 200, '{"success": true}')

    def test_delete_404(self):
        self.mocked['post']().delete.side_effect = NotExistsException('foo')

        response = self.client.delete('/post/unknown-post.md')

        self._compare_assertions(response, 404, self.error_404_response)

    def test_bulk_update(self):
        self.skipTest("'test_bulk_update' is not implemented yet.")

    def test_bulk_delete(self):
        self.skipTest("'test_bulk_delete' is not implemented yet.")

    def _compare_assertions(self, response, expected_code, expected_data):
        self.assertEqual(response.status_code, expected_code)

        self.assertIsInstance(response.data, str)
        self.assertEqual(response.data, expected_data)

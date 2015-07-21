# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""Test cases for post controller."""

from app import app
import unittest
import mock
import json


class TestCase(unittest.TestCase):
    """Test cases for PostView."""

    client = app.test_client()

    @mock.patch('app.models.post.Post.list')
    def test_listing(self, mocked):
        mocked.return_value = []

        response = self.client.get('/post')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    @mock.patch('app.models.post.Post.read')
    def test_get(self, mocked):
        mocked.return_value = {}

        response = self.client.get('/post/some-post.md')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)

    @mock.patch('app.models.post.Post.save')
    def test_create(self, mocked):
        mocked.return_value = {}

        response = self.client.post('/post', data={})

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)

    @mock.patch('app.models.post.Post.update')
    def test_update(self, mocked):
        mocked.return_value = {}

        response = self.client.put('/post/some-post.md')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)

    @mock.patch('app.models.post.Post.delete')
    def test_delete(self, mocked):
        mocked.return_value = {}

        response = self.client.delete('/post/some-post.md')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), dict)

    def test_bulk_update(self):
        self.skipTest("'test_bulk_update' is not implemented yet.")

    def test_bulk_delete(self):
        self.skipTest("'test_bulk_delete' is not implemented yet.")

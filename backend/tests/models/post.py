# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""Test cases for post model."""

import unittest
import json
from app.blueprints.post.post import PostReader, PostModel, PostSerializer
from fixtures.post import MockedFs, post_raw, post_data, post_json


class PostTestCase(unittest.TestCase):
    """Test cases for post model."""

    def setUp(self):
        """Start patching objects."""
        self.post = PostReader(MockedFs())

    def tearDown(self):
        """Stop patching objects."""
        pass

    def test_list(self):
        """Test for list method."""
        result = self.post.list()

        self.assertIsInstance(result, list)

    def test_read(self):
        """Test for read method."""
        result = self.post.read('post-id')

        self.assertIsInstance(result, PostModel)

    def test_save(self):
        """Test for save method."""
        result = self.post.save('post-id', **post_data)

        self.assertIsInstance(result, PostModel)

    def test_update(self):
        """Test for update method."""
        result = self.post.update('post-id', **post_data)

        self.assertIsInstance(result, PostModel)

    def test_delete(self):
        """Test for delete method."""
        result = self.post.delete('post-id')

        self.assertIsInstance(result, PostModel)


class PostModelTestCase(unittest.TestCase):
    def test_returns(self):
        result = PostModel(**post_data)

        for key in post_data.iterkeys():
            self.assertEqual(result[key], post_data[key])

    def test_update(self):
        self.skipTest('test_update')

    def test_decode(self):
        result = PostModel.decode(post_raw)

        self.assertIsInstance(result, PostModel)
        for key in post_data.iterkeys():
            self.assertEqual(result[key], post_data[key])

    def test_encode(self):
        post = PostModel(**post_data)
        result = PostModel.encode(post)

        self.assertIsInstance(result, str)
        self.assertIsInstance(post_raw, str)
        self.assertEqual(result, post_raw)


class PostSerializerTestCase(unittest.TestCase):
    def test_some(self):
        post = PostModel(**post_data)

        result = json.dumps(post, cls=PostSerializer)

        self.assertEqual(result, post_json)

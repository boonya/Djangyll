# -*- coding: utf-8 -*-
__author__ = 'boonya'
"""Test cases for post model."""
import unittest
import json
from datetime import datetime
from app.models.post import Post
from app.models.post import PostModel
from app.models.post import PostSerializer
from fixtures.post import MockedFs
from fixtures.post import post_raw
from fixtures.post import post_data
from fixtures.post import post_json


class PostTestCase(unittest.TestCase):
    """Test cases for post model."""

    def setUp(self):
        """Start patching objects."""
        self.post = Post(MockedFs())

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
        post_data['id'] = 'post-id'
        result = self.post.save(**post_data)

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

        post_data['id'] = None

        self.assertDictEqual(result.__dict__, post_data)
        self.assertIsInstance(result['featured'], bool)
        self.assertIsInstance(result['layout'], unicode)
        self.assertIsInstance(result['title'], unicode)
        self.assertIsInstance(result['slug'], unicode)
        self.assertIsInstance(result['date'], datetime)
        self.assertIsInstance(result['category'], unicode)
        self.assertIsInstance(result['cat_slug'], unicode)
        self.assertIsInstance(result['language'], unicode)
        self.assertIsInstance(result['permalink'], unicode)
        self.assertIsInstance(result['body'], unicode)

    def test_decode(self):
        result = PostModel.decode(post_raw)

        post_data['id'] = None

        self.assertIsInstance(result, PostModel)
        self.assertDictEqual(result.__dict__, post_data)

    def test_encode(self):
        post = PostModel(**post_data)
        result = PostModel.encode(post)

        self.assertIsInstance(result, basestring)

        result = PostModel.decode(post_raw)

        post_data['id'] = None

        self.assertIsInstance(result, PostModel)
        self.assertDictEqual(result.__dict__, post_data)


class PostSerializerTestCase(unittest.TestCase):
    def test_some(self):
        post_data['id'] = 'post-id'
        post = PostModel(**post_data)

        result = json.dumps(post, cls=PostSerializer)

        self.assertEqual(result, post_json)

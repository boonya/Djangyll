# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""Test cases for post model."""

import unittest
from app.models.post import Post
from app.models.post import PostModel
from fixtures.post import MockedFs
from fixtures.post import post_data


class ModelPostTestCase(unittest.TestCase):
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

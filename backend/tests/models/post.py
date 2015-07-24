# -*- coding: utf-8 -*-
__author__ = 'boonya'

"""Test cases for post model."""

import unittest
import mock
from app.models.post import Post


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

        self.assertIsInstance(result, dict)
        self.assertIn("meta", result)
        self.assertIn("body", result)

    def test_save(self):
        """Test for save method."""
        self.skipTest("'test_save' is not implemented yet.")

        result = self.post.save(data='data')

        self.assertIsInstance(result, dict)
        self.assertIn("meta", result)
        self.assertIn("body", result)

    def test_update(self):
        """Test for update method."""
        self.skipTest("'test_update' is not implemented yet.")

        result = self.post.update('post-id', data='data')

        self.assertIsInstance(result, dict)
        self.assertIn("meta", result)
        self.assertIn("body", result)

    def test_delete(self):
        """Test for delete method."""
        self.skipTest("'test_delete' is not implemented yet.")

        result = self.post.delete('post-id')

        self.assertIsInstance(result, dict)
        self.assertIn("meta", result)
        self.assertIn("body", result)


class MockedFs(object):
    def list(self):
        return []

    def read(self, post_id):
        return """
        ---
        layout: post
        joomla_content_id: 1
        title: "Про нас"
        slug: about
        #date: 2010-10-25 22:00:00.000000000 +03:00
        category: Uncategorised
        cat_slug: uncategorised
        featured: 0
        language: uk-UA
        permalink: "/about.html"
        ---
        ###Title of post
        simple text
        """

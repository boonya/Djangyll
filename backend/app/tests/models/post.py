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
        self.patcher_fs = mock.patch('app.models.post.Post.file_system')
        self.mocked_fs = self.patcher_fs.start()

        self.mocked_post = Post()
        self.mocked_post.file_system = self.mocked_fs

    def tearDown(self):
        """Stop patching objects."""
        self.mocked_fs = self.patcher_fs.stop()

    def test_list(self):
        """Test for list method."""
        self.mocked_post.file_system.list.return_value = []

        result = self.mocked_post.list()

        self.assertIsInstance(result, list)

    def test_read(self):
        """Test for read method."""
        self.mocked_post.file_system.read.return_value = """
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

        result = self.mocked_post.read('post-id')

        self.assertIsInstance(result, dict)
        self.assertIn("meta", result)
        self.assertIn("body", result)

    def test_save(self):
        """Test for save method."""
        self.skipTest("save is not implemented yet.")

    def test_update(self):
        """Test for update method."""
        self.skipTest("update is not implemented yet.")

    def test_delete(self):
        """Test for delete method."""
        self.skipTest("delete is not implemented yet.")

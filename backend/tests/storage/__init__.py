# -*- coding: utf-8 -*-
__author__ = 'boonya'


import unittest
import mock
from app.storage import Storage


class StorageTestCase(unittest.TestCase):
    def setUp(self):
        """Start patching objects."""
        self.patcher = mock.patch('app.storage.DirectFs')
        self.mocked = self.patcher.start()

        self.storage = Storage()

    def tearDown(self):
        """Stop patching objects."""
        self.patcher.stop()

    def test_listing(self):
        """Test for list method."""
        result = self.storage.listing()

        self.assertIsNone(result)

    def test_read(self):
        """Test for read method."""
        result = self.storage.read('post-id')

        self.assertIsNone(result)

    def test_create(self):
        """Test for save method."""
        result = self.storage.create('post-id', {})

        self.assertIsNone(result)

    def test_update(self):
        """Test for update method."""
        result = self.storage.update('post-id', {})

        self.assertIsNone(result)

    def test_delete(self):
        """Test for delete method."""
        result = self.storage.delete('post-id')

        self.assertIsNone(result)
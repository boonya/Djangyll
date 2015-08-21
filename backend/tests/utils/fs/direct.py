# -*- coding: utf-8 -*-
__author__ = 'boonya'

import unittest
import os
from app import BASE_DIR
from app.utils.fs.direct import Direct
from app.utils.fs.exception import NotExistsException


class DirectTestCase(unittest.TestCase):
    container_path = os.path.join(BASE_DIR, '../tmp')

    mock_files = {
        'first.md': 'Data of first file',
        'second.md': 'Data of second file'
    }

    files_to_cleanup = []

    def setUp(self):
        for (path, data) in self.mock_files.iteritems():
            self.create_file(path, data)

    def tearDown(self):
        for path in self.files_to_cleanup:
            self.remove_file(path)

    def test_wrong_init(self):
        with self.assertRaises(ValueError):
            Direct('unknown-path')

    def test_list(self):
        mocked_list = ['.gitignore']
        mocked_list += self.mock_files.keys()

        fs = Direct(self.container_path)
        result = fs.list()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, mocked_list)

    def test_read(self):
        fs = Direct(self.container_path)
        result = fs.read('first.md')

        self.assertEqual(result, 'Data of first file')

    def test_read_unknown(self):
        with self.assertRaises(NotExistsException):
            fs = Direct(self.container_path)
            fs.read('unknown.md')

    def test_write_new(self):
        path = 'third.md'
        data = 'Data of third file'

        fs = Direct(self.container_path)
        result = fs.write(path, data)

        self.files_to_cleanup.append(path)

        self.assertEqual(result, data)

    def test_write_existing(self):
        path = 'second.md'
        data = 'Updated data of second file'

        fs = Direct(self.container_path)
        result = fs.write(path, data)

        self.assertEqual(result, data)

        with open(os.path.join(self.container_path, path), 'r') as fh:
            content = fh.read()

        self.assertEqual(content, data)

    def test_remove(self):
        fs = Direct(self.container_path)
        fs.remove('second.md')

        listing = [f for f in os.listdir(self.container_path) if
                   os.path.isfile(os.path.join(self.container_path, f))]

        self.assertEqual(len(listing), 2)

    def test_remove_unknown(self):
        with self.assertRaises(NotExistsException):
            fs = Direct(self.container_path)
            fs.remove('unknown.md')

    def create_file(self, path, data):
        file_path = os.path.join(self.container_path, path)

        with open(file_path, 'w') as fh:
            fh.write(data)

        self.files_to_cleanup.append(path)

    def remove_file(self, path):
        file_path = os.path.join(self.container_path, path)
        if not os.path.isfile(file_path):
            return None

        os.remove(file_path)

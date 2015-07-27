# -*- coding: utf-8 -*-
__author__ = 'boonya'

import unittest
import os
from app import app
from app.utils.fs.direct import Direct
from app.utils.fs.exception import NotExistsException


class DirectTestCase(unittest.TestCase):
    mock_files = {
        'first.md': 'Data of first file',
        'second.md': 'Data of second file'
    }

    files_to_cleanup = []

    def setUp(self):
        self.container_path = os.path.join(app.root_path, '../tmp')
        self.fs = Direct(self.container_path)
        for (path, data) in self.mock_files.iteritems():
            self.create_file(path, data)
            self.files_to_cleanup.append(path)

    def tearDown(self):
        for path in self.files_to_cleanup:
            file_path = os.path.join(self.container_path, path)
            self.remove_file(file_path)

    def test_list(self):
        result = self.fs.list()

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

    def test_read(self):
        result = self.fs.read('first.md')

        self.assertEqual(result, 'Data of first file')

    def test_read_unknown(self):
        path = 'unknown.md'

        try:
            self.fs.read(path)
        except NotExistsException, exc:
            self.assertEqual(exc.args[0], "'%s' is unknown file." % path)
            return None
        except Exception:
            self.fail("We wait an NotExistsException exception")

        self.fail("We wait an exception")

    def test_write_new(self):
        path = 'third.md'
        data = 'Data of third file'

        result = self.fs.write(path, data)

        self.files_to_cleanup.append(path)

        self.assertEqual(result, data)

    def test_write_existing(self):
        path = 'second.md'
        data = 'Updated data of second file'

        result = self.fs.write(path, data)

        self.assertEqual(result, data)

        with open(os.path.join(self.container_path, path), 'r') as fh:
            content = fh.read()

        self.assertEqual(content, data)

    def test_remove(self):
        self.fs.remove('second.md')

        listing = [f for f in os.listdir(self.container_path) if
                   os.path.isfile(os.path.join(self.container_path, f))]

        self.assertEqual(len(listing), 2)

    def test_remove_unknown(self):
        path = 'unknown.md'
        try:
            self.fs.remove(path)
        except NotExistsException, exc:
            self.assertEqual(exc.args[0], "'%s' is unknown file." % path)
            return None
        except Exception:
            self.fail("We wait an NotExistsException exception")

        self.fail("We wait an exception")

    def create_file(self, path, data):
        file_path = os.path.join(self.container_path, path)

        with open(file_path, 'w') as fh:
            fh.write(data)

    def remove_file(self, path):
        file_path = os.path.join(self.container_path, path)

        if not os.path.isfile(os.path.join(self.container_path, file_path)):
            return None

        os.remove(file_path)

"""Test cases for post module."""

from django.test import TestCase
import mock
import json


class TestPostView(TestCase):

    """Test cases for post.view."""

    def setUp(self):
        """Start patching objects."""
        self.patcher_init = mock.patch('apps.post.views.PostView.__init__')
        self.patcher_reader = mock.patch('apps.post.views.PostView.reader')
        self.mocked_init = self.patcher_init.start()
        self.mocked_reader = self.patcher_reader.start()
        self.mocked_init.return_value = None

    def tearDown(self):
        """Stop patching objects."""
        self.patcher_init.stop()
        self.patcher_reader.stop()

    def test_get_listing(self):
        """Test coverage for get listing of posts."""
        mocked_response = ['first', 'second']

        self.mocked_reader.list.return_value = mocked_response

        response = self.client.get('/post')

        self.assertEqual(200, response.status_code)
        self.assertEqual(json.dumps(mocked_response), response.content)

        response = self.client.get('/post/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(json.dumps(mocked_response), response.content)

    def test_get_one(self):
        """Test coverage for get one post."""
        mocked_response = {'some': 'data'}

        self.mocked_reader.read.return_value = mocked_response

        response = self.client.get('/post/post-id')

        self.assertEqual(200, response.status_code)
        self.assertEqual(json.dumps(mocked_response), response.content)

    def test_post(self):
        """Test coverage for create post."""
        mocked_response = True

        self.mocked_reader.save.return_value = mocked_response

        response = self.client.post('/post', {'content': 'data'})

        self.assertEqual(200, response.status_code)
        self.assertEqual(json.dumps(mocked_response), response.content)

    def test_put_one(self):
        """Test coverage for update one post."""
        mocked_response = True

        self.mocked_reader.update.return_value = mocked_response

        response = self.client.put('/post/post-id', "content=data")

        self.assertEqual(200, response.status_code)
        self.assertEqual(json.dumps(mocked_response), response.content)

    def test_put_bulk(self):
        """Test coverage for bulk update."""
        mocked_response = True

        self.mocked_reader.update.return_value = mocked_response

        response = self.client.put('/post', "id=1&id=2&id=3&content=data")

        self.assertEqual(200, response.status_code)
        self.assertEqual(json.dumps(mocked_response), response.content)

    def test_delete_one(self):
        """Test coverage for delete one post."""
        mocked_response = True

        self.mocked_reader.remove.return_value = mocked_response

        response = self.client.delete('/post/post-id')

        self.assertEqual(200, response.status_code)
        self.assertEqual(json.dumps(mocked_response), response.content)

    def test_delete_bulk(self):
        """Test coverage for bulk delete."""
        mocked_response = True

        self.mocked_reader.remove.return_value = mocked_response

        response = self.client.delete('/post', "id=1&id=2&id=3")

        self.assertEqual(200, response.status_code)
        self.assertEqual(json.dumps(mocked_response), response.content)

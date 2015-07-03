from django.test import TestCase
from mock import Mock
from apps.post.models import Reader


class MyTestCase(TestCase):

    def test1(self):
        # mocked_reader = Mock(Reader)
        # mocked_reader.list.return_value = ['first', 'second']

        response = self.client.get('/post/')

        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.content, str)

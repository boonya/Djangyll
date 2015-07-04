"""Request middleware."""
from django.http import QueryDict
import json


class ParseAndSetRawRequestDataIntoPost(object):

    """Middleware for adaptation REST API requests with Django."""

    @staticmethod
    def process_request(request):
        """Manipulate the request object before passing it to view functions.

        :param HttpRequest request:
        :return:
        """
        if request.method not in ['PUT', 'DELETE']:
            return None

        try:
            # @TODO: Need to fix this problem
            # QueryDict.update(data) saves recursive dictionaries wrong.
            #
            # {"arg1": ["val1", "val1.1"], "arg2": "val2"}
            # {u'arg1': [u'val1', u'val1.1'], u'arg2': u'val2'}
            # <QueryDict: {u'arg1': [[u'val1', u'val1.1']], u'arg2': [u'val2']}
            #
            # "arg1=val1&arg1=val1.1&arg2=val2"
            # <QueryDict: {u'arg1': [u'val1', u'val1.1'], u'arg2': [u'val2']}>
            data = json.loads(request.body)
            request.POST = QueryDict('', mutable=True)
            request.POST.update(data)
            request.POST._mutable = False
        except ValueError:
            request.POST = QueryDict(request.body)

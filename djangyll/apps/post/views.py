from django.views.generic import View
from utils.response import JsonResponse
from .models import Reader


class PostView(View):
    """
    Configurations CRUD
    """

    def get(self, request, post_id=None, *args, **kwargs):
        reader = Reader()

        response = {
            'data': None
        }

        if not post_id:
            response['data'] = reader.list()
        else:
            response['data'] = reader.read(post_id)

        return JsonResponse(response)

from django.views.generic import View
from utils.response import JsonResponse, JsonResponseNotFound, JsonResponseBadRequest
from .models import Reader, BadFile
from utils.file_system import NotExistsException


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
            try:
                response['data'] = reader.read(post_id)
            except NotExistsException, exc:
                return JsonResponseNotFound(exc.message)
            except BadFile, exc:
                return JsonResponseBadRequest(exc.message)

        return JsonResponse(response)

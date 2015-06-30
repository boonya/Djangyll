from django.views.generic import View
import html2text
from utils.response import JsonResponse, JsonResponseNotFound, JsonResponseBadRequest
from .models import Reader, BadFile
from utils.file_systems.interface import NotExistsException


class PostView(View):
    """
    Configurations CRUD
    """

    def get(self, request, post_id=None, *args, **kwargs):
        reader = Reader()

        response = {'data': []}

        if not post_id:
            response['data'] = reader.list()
        else:
            try:
                response['data'] = reader.read(post_id)

                if 'html_to_md' == request.GET.get('convert', None):
                    response['data']['body'] = html2text.html2text(response['data']['body'])

            except NotExistsException, exc:
                return JsonResponseNotFound(exc.message)
            except BadFile, exc:
                return JsonResponseBadRequest(exc.message)

        return JsonResponse(response)

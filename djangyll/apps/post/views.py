from django.views.generic import View
import html2text
from utils.response import JsonResponse, JsonResponseNotFound, JsonResponseBadRequest
from .models import Reader, BadFile
from utils.file_systems.interface import NotExistsException


class PostView(View):
    """
    Configurations CRUD
    """
    reader = Reader(site_id=1)

    def get(self, request, post_id=None, *args, **kwargs):
        """
        Get request handler for getting listing of posts or data of concrete post.
        """

        if not post_id:
            return JsonResponse(self.reader.list())

        try:
            data = self.reader.read(post_id)

            if 'html_to_md' == request.GET.get('convert', None):
                data['body'] = html2text.html2text(data['body'])

            return JsonResponse(data)

        except NotExistsException, exc:
            return JsonResponseNotFound(exc.message)

        except BadFile, exc:
            return JsonResponseBadRequest(exc.message)

    def post(self, request, *args, **kwargs):
        """
        Post request handler for creating new posts.
        """

        data = request.POST
        return JsonResponse(data)

    def put(self, request, post_id=None, *args, **kwargs):
        """
        Put request handler for bulk update posts or concrete post.
        """

        data = request.POST
        return JsonResponse(data)

    def delete(self, request, post_id=None, *args, **kwargs):
        """
        Delete request handler for bulk delete posts or concrete post.
        """

        data = request.POST
        return JsonResponse(data)

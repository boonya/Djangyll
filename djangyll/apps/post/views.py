"""Post view."""
from django.views.generic import View
from utils.response import JsonResponse, JsonResponseNotFound, JsonResponseBadRequest
from utils.file_systems.interface import NotExistsException
from .models import Reader, BadFile
import reasons


class PostView(View):

    """Configurations CRUD."""

    reader = None

    def __init__(self):
        super(PostView, self).__init__()
        self.reader = Reader()

    def get(self, request, post_id=None, *args, **kwargs):
        """Get request handler for getting listing of posts or data of concrete post."""
        try:
            if post_id:
                data = self.reader.read(post_id)
            else:
                data = self.reader.list()

            return JsonResponse(data)

        except NotExistsException:
            return JsonResponseNotFound(reasons.DOES_NOT_EXIST)

        except BadFile:
            return JsonResponseBadRequest(reasons.BAD_FILE)

    def post(self, request, *args, **kwargs):
        """Post request handler for creating new posts."""

        data = request.POST
        return JsonResponse(data)

    def put(self, request, post_id=None, *args, **kwargs):
        """Put request handler for bulk update posts or concrete post."""
        if not post_id and not request.POST.get('id', None):
            return JsonResponseBadRequest(reasons.NO_ID)

        data = request.POST
        return JsonResponse(data)

    def delete(self, request, post_id=None, *args, **kwargs):
        """Delete request handler for bulk delete posts or concrete post."""
        if not post_id and not request.POST.get('id', None):
            return JsonResponseBadRequest(reasons.NO_ID)

        data = request.POST
        return JsonResponse(data)

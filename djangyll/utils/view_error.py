from utils.response import *


class ViewMiddleware(object):
    codes_mapping = {
        400: JsonResponseBadRequest,
        403: JsonResponseForbidden,
        404: JsonResponseNotFound,
        410: JsonResponseGone,
        500: JsonResponseServerError
    }

    def process_response(self, request, response):
        response_class = self.codes_mapping.get(response.status_code, None)
        if response_class:
            response = response_class(response.reason_phrase)

        return response

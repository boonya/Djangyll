from django.http import JsonResponse as BaseJsonResponse


class JsonResponse(BaseJsonResponse):
    pass


class JsonBaseError(BaseJsonResponse):
    def __init__(self, data, **kwargs):
        if not isinstance(data, list):
            data = [data]
        super(JsonBaseError, self).__init__(data={'reasons': data}, **kwargs)


class JsonResponseBadRequest(JsonBaseError):
    status_code = 400


class JsonResponseNotFound(JsonBaseError):
    status_code = 404


class JsonResponseForbidden(JsonBaseError):
    status_code = 403


class JsonResponseGone(JsonBaseError):
    status_code = 410


class JsonResponseServerError(JsonBaseError):
    status_code = 500

from django.views.generic import View
from django.http import JsonResponse
from json import dumps

class ConfigurationView(View):
    """
    Configurations CRUD
    """

    def get(self, request, app_id=None, *args, **kwargs):
        """
        :param request:
        :param app_id:
        :param args:
        :param kwargs:
        :return:
        """
        response = {
            # 'request': dumps(request),
            'app_id': app_id,
            'args': args,
            'kwargs': kwargs
        }
        return JsonResponse(response, safe=False)

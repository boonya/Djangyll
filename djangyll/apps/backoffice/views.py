from django.shortcuts import render
from django.views.generic import View


class BackofficeView(View):
    """
    Back office application view.
    """

    template_name = 'backoffice/layout.html'

    def dispatch(self, *args, **kwargs):
        return super(BackofficeView, self).dispatch(*args, **kwargs)

    def get(self, request):
        template_params = dict()

        return render(request, self.template_name, template_params, content_type="text/html")
"""
Back office application urls.
"""

from django.conf.urls import patterns, url
from .views import BackofficeView

urlpatterns = patterns(
    '',
    url(r'^$', BackofficeView.as_view(), name='back-office'),
    url(r'^(?P<path>.+)$', 'django.views.static.serve', {'document_root': 'static/'},
        name='static_url')
)
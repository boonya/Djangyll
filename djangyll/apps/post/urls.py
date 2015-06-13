"""
Post CRUD urls.
"""

from django.conf.urls import patterns, url
from .views import PostView


urlpatterns = patterns(
    '',
    url(r'^(?P<post_id>.*)/?$', PostView.as_view(), name='post-view')
)
"""
Post CRUD urls.
"""

from django.conf.urls import url
from .views import PostView


urlpatterns = [
    url(r'^(?P<post_id>.*)/?$', PostView.as_view(), name='post-view')
]

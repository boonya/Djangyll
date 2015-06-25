from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^back-office/', include('apps.backoffice.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/', include('apps.post.urls'))
)

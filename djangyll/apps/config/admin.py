from django.contrib import admin

from .models import User, WebSite, FileSystem

admin.site.register(User)
admin.site.register(WebSite)
admin.site.register(FileSystem)

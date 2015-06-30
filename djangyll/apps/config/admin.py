from django.contrib import admin

from .models import User, WebSite, FileSystem, FsOption, FsOptValue

admin.site.register(User)
admin.site.register(WebSite)
admin.site.register(FileSystem)
admin.site.register(FsOption)
admin.site.register(FsOptValue)

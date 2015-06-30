from django.db import models


class User(models.Model):
    email = models.EmailField()
    web_site = models.ManyToManyField('WebSite')

    def __str__(self):
        return self.email


class WebSite(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    domain = models.URLField()
    file_system = models.ForeignKey('FileSystem')
    opt_values = models.ManyToManyField('FsOptValue')

    def __str__(self):
        return self.title


class FileSystem(models.Model):
    title = models.CharField(max_length=30)
    options = models.ManyToManyField('FsOption')

    def __str__(self):
        return self.title


class FsOption(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class FsOptValue(models.Model):
    value = models.CharField(max_length=100)
    option = models.ForeignKey('FsOption')

    def __str__(self):
        return self.value

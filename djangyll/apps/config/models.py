from django.db import models


class User(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    web_site = models.ManyToManyField('WebSite')

    def __str__(self):
        return self.title


class WebSite(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    domain = models.URLField()
    file_system = models.ForeignKey('FileSystem')

    def __str__(self):
        return self.title


class FileSystem(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Option(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

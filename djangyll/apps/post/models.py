import re

import yaml
import markdown

from utils.file_systems.direct import Direct
from apps.config.models import WebSite


class Reader(object):
    file_system = None

    def __init__(self):
        web_site = WebSite.objects.get(pk=1)
        # fs = web_site.file_system
        options = web_site.opt_values.all()
        path = options[0].value
        # path = '/Users/boonya/Documents/codebase/miks.org.ua/jekyll-version/src/_posts'

        self.file_system = Direct(path)

    def list(self):
        """
        Returns listing of post`s names.

        :return list:
        """
        return self.file_system.list()

    def read(self, post_id):
        """
        Returns metadata & content of post.

        :param string post_id:
        :return dict:
        """
        raw_data = self.file_system.read(post_id)

        entries = re.split("---\n+", raw_data)

        if not 3 == len(entries):
            raise BadFile("The content of '%s' is invalid." % post_id)

        meta = yaml.load(entries[1])
        body = markdown.markdown(unicode(entries[2], "utf-8"))

        return {
            'meta': meta,
            'body': body
        }


class BadFile(Exception):
    pass

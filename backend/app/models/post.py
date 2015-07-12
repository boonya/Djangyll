# -*- coding: utf-8 -*-
__author__ = 'boonya'
"""Model of post module."""
import re
import yaml
import markdown
from app.utils.fs.direct import Direct


class Post(object):
    """Files reader class."""

    file_system = None

    def __init__(self):
        """Simple Constructor.

        It should prepare object of adapter for FS which was preselected for
        current site.
        :return:
        """

        # TODO: Do something with this shit. It have to be customizable with some settings.
        path = '/Users/boonya/Documents/codebase/miks.org.ua/jekyll-version/src/_posts'
        self.file_system = Direct(path)

    def list(self):
        """Return listing of files`s names.

        :return list:
        """
        return self.file_system.list()

    def read(self, post_id):
        """Return metadata & content of post.

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

    def save(self, **kwargs):
        """Create new file of article.

        :param kwargs:
        :return dict:
        """
        raise NotImplementedError('Not implemented yet.')

    def update(self, post_id, **kwargs):
        """Update file of article.

        :param string post_id:
        :param kwargs:
        :return dict:
        """
        raise NotImplementedError('Not implemented yet.')


class BadFile(Exception):
    """Special exception for this module."""

    def __init__(self, *args, **kwargs):
        """Just constructor.

        :param args:
        :param kwargs:
        :return:
        """
        super(BadFile, self).__init__(args, kwargs)

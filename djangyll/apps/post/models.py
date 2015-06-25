from utils.direct_fs import DirectFs
import yaml
import re
from bs4 import BeautifulSoup
import markdown


class Reader(object):
    file_system = None

    def __init__(self):
        self.file_system = DirectFs('/Users/boonya/Documents/miks/jekyll-static/src/_posts')

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

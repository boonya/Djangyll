# -*- coding: utf-8 -*-
__author__ = 'boonya'
"""Model of posts."""
import re
import yaml
import markdown
import json


class Post(object):
    """Files reader class."""

    def __init__(self, FsAdapter):
        """Simple Constructor.

        It should prepare object of adapter for FS which was preselected for
        current site.
        :return:
        """

        self.file_system = FsAdapter

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
        return PostModel.decode(raw_data)

    def save(self, **kwargs):
        """Create new file of article.

        :param kwargs:
        :return dict:
        """
        post_id = kwargs['id']
        post = PostModel(**kwargs)
        if post_id in self.file_system.list():
            raise BadFile("File '%s' already exists." % post_id)
        raw_data = self.file_system.write(post_id, PostModel.encode(post))
        return PostModel.decode(raw_data)

    def update(self, post_id, **kwargs):
        """Update file of article.

        :param string post_id:
        :param kwargs:
        :return dict:
        """
        post = self.read(post_id)
        post.update(**kwargs)
        raw_data = self.file_system.write(post_id, PostModel.encode(post))
        return PostModel.decode(raw_data)

    def delete(self, post_id, **kwargs):
        """Delete file of article.

        :param string post_id:
        :param kwargs:
        :return dict:
        """
        post = self.read(post_id)
        self.file_system.remove(post_id)
        return post


class PostModel(object):
    attributes = ('id', 'layout', 'title', 'slug', 'date', 'category',
                  'cat_slug', 'featured', 'language', 'permalink', 'body')

    def __init__(self, **kwargs):
        for attr in self.attributes:
            value = None
            if attr in kwargs:
                value = kwargs[attr]
            self.__setitem__(attr, value)

    def __delitem__(self, key):
        self.__delattr__(key)

    def __getitem__(self, key):
        return self.__getattribute__(key)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def update(self, **kwargs):
        for attr in self.attributes:
            if attr in kwargs:
                self.__setitem__(attr, kwargs[attr])

    @staticmethod
    def decode(raw_data):
        entries = re.split("---\n+", raw_data)

        if 3 != len(entries):
            raise BadFile("The content is invalid.")

        meta = yaml.load(entries[1])
        body = markdown.markdown(unicode(entries[2], "utf-8"))

        return PostModel(body=body, **meta)

    @staticmethod
    def encode(model):
        if not isinstance(model, PostModel):
            raise ValueError("Is an instance of unexpected class.")
        meta = {key: value for key, value in model.__dict__.iteritems() if
                'body' not in key}
        body = model.__dict__.get('body', None)
        meta = yaml.dump(meta, default_flow_style=False) + "\n"
        return "---\n".join(['', meta, body])


class PostSerializer(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, PostModel):
            return super(PostSerializer, self).default(obj)

        # @TODO: Need to make more common.
        if obj.date:
            obj.date = obj.date.isoformat()

        return obj.__dict__


class BadFile(Exception):
    """Special exception for this module."""

    def __init__(self, *args, **kwargs):
        """Just constructor.

        :param args:
        :param kwargs:
        :return:
        """
        super(BadFile, self).__init__(args, kwargs)

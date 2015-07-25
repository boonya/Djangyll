# -*- coding: utf-8 -*-
__author__ = 'boonya'
"""Model of posts."""
import re
import yaml
import json


class Post(object):
    """Files reader class."""

    def __init__(self, fs_adapter):
        """Simple Constructor.

        :param fs_adapter:
        :return:
        """

        self.file_system = fs_adapter

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
        post = PostModel.decode(raw_data)
        post['id'] = post_id
        return post

    def save(self, **kwargs):
        """Create new file of article.

        :param kwargs:
        :return dict:
        """
        post_id = kwargs['id']
        post = PostModel(**kwargs)
        if post_id in self.file_system.list():
            raise BadFile("File '%s' already exists." % post_id)
        self.file_system.write(post_id, PostModel.encode(post))
        return post

    def update(self, post_id, **kwargs):
        """Update file of article.

        :param string post_id:
        :param kwargs:
        :return dict:
        """
        post = self.read(post_id)
        post.update(**kwargs)
        self.file_system.write(post_id, PostModel.encode(post))
        return post

    def delete(self, post_id):
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
        if isinstance(value, str):
            value = unicode(value, "utf-8")
        self.__setattr__(key, value)

    def update(self, **kwargs):
        for attr in self.attributes:
            if attr in kwargs:
                self.__setitem__(attr, kwargs[attr])

    @staticmethod
    def decode(raw_data):
        """Decode passed raw data to model object.

        :param str raw_data:
        :return PostModel:
        """
        entries = re.split("---\n+", raw_data)

        if 3 != len(entries):
            raise BadFile("The content is invalid.")

        return PostModel(body=entries[2], **yaml.load(entries[1]))

    @staticmethod
    def encode(model):
        """Encode passed model to raw post data.

        :param PostModel model:
        :return str:
        """
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
        if obj['date']:
            obj['date'] = obj['date'].isoformat()

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

# -*- coding: utf-8 -*-
__author__ = 'boonya'

import re
import yaml
from ...utils.serializer import Serializer


class PostReader(object):
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

    def save(self, post_id, **kwargs):
        """Create new file of article.

        :param kwargs:
        :return dict:
        """
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
    attributes = ('layout', 'permalink', 'title', 'body')
    unicode = ('title', 'body')
    data = {}

    def __init__(self, **kwargs):
        for attr in self.attributes:
            self.data[attr] = kwargs.get(attr, None)

    def __getitem__(self, key):
        return self.data.get(key, None)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __dict__(self):
        return self.data

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

        return PostModel(body=unicode(entries[2], "utf-8"),
                         **yaml.load(entries[1]))

    @staticmethod
    def encode(model):
        """Encode passed model to raw post data.

        :param PostModel model:
        :return str:
        """
        if not isinstance(model, PostModel):
            raise ValueError("Is an instance of unexpected class.")

        meta_dict = {key: value for key, value in model.__dict__().iteritems()
                     if key not in ('body', 'id')}

        meta = yaml.dump(meta_dict, default_flow_style=False, encoding=None,
                         allow_unicode=True)

        result = "---\n".join(['', meta, model['body']]).encode('utf8')

        return result


class PostSerializer(Serializer):
    def default(self, obj):
        if not isinstance(obj, PostModel):
            return super(PostSerializer, self).default(obj)

        return obj.__dict__()


class BadFile(Exception):
    """Special exception for this module."""

    def __init__(self, *args, **kwargs):
        """Just constructor.

        :param args:
        :param kwargs:
        :return:
        """
        super(BadFile, self).__init__(args, kwargs)

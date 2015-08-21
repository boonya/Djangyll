# -*- coding: utf-8 -*-
__author__ = 'boonya'

import json
from flask import Blueprint
from ...utils.request import Request
from ...utils.response import Response
from ...utils.fs import Fs
from ...utils.fs.exception import NotExistsException
from ...reasons import errors
from .post import Post
from .post import PostSerializer

post = Blueprint('post', __name__, url_prefix='/post')


@post.route('/', methods=['GET'])
def listing():
    """Get listing.

    :return list:
    """
    model = Post(Fs.get())

    posts = model.list()

    return Response.success(posts)


@post.route('/<post_id>', methods=['GET'])
def get(post_id):
    """Get concrete post.

    :param str post_id:
    :return dict:
    """
    model = Post(Fs.get())

    try:
        response = model.read(post_id)
    except NotExistsException:
        return Response.failure(errors.DOES_NOT_EXIST, code=404)

    return Response.success(response, serializer=PostSerializer)


@post.route('/', methods=['POST'])
def create():
    """Create new post.

    :return dict:
    """
    model = Post(Fs.get())

    response = model.save(**Request.dict())

    return Response.success(response, serializer=PostSerializer)


@post.route('/<post_id>', methods=['PUT'])
def update(post_id):
    """Update concrete post.

    :param str post_id:
    :return dict:
    """
    model = Post(Fs.get())

    try:
        response = model.update(post_id, **Request.dict())
    except NotExistsException:
        return Response.failure(errors.DOES_NOT_EXIST, 404)

    return Response.success(response, serializer=PostSerializer)


@post.route('/<post_id>', methods=['DELETE'])
def delete(post_id):
    """Delete concrete post.

    :param str post_id:
    :return dict:
    """
    model = Post(Fs.get())

    try:
        response = model.delete(post_id)
    except NotExistsException:
        return Response.failure(errors.DOES_NOT_EXIST, 404)

    return Response.success(response, serializer=PostSerializer)


@post.route('/', methods=['PUT'])
def bulk_update():
    """Bulk update.

    :return list:
    """
    return Response.success(json.dumps("Bulk update"))


@post.route('/', methods=['DELETE'])
def bulk_delete():
    """Bulk delete.

    :return list:
    """
    return Response.success(json.dumps("Bulk delete"))

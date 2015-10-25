# -*- coding: utf-8 -*-
__author__ = 'boonya'

from flask import Blueprint
from ...utils.request import Request
from ...utils.response import Response
# from ...utils.fs import Fs
# from ...utils.fs.exception import NotExistsException

from ...storage import Storage
from ...storage import NotExistsException

# from .post import PostReader
from .post import PostSerializer
from werkzeug.exceptions import NotFound

post = Blueprint('post', __name__, url_prefix='/post')


@post.route('/', methods=['GET'])
def listing():
    """Get listing.

    :return list:
    """
    storage = Storage()
    result = storage.listing()
    return Response.success(result)


@post.route('/<post_id>', methods=['GET'])
def get(post_id):
    """Get concrete post.

    :param str post_id:
    :return dict:
    """
    reader = Storage()

    try:
        result = reader.read(post_id)
    except NotExistsException:
        raise NotFound()

    return Response.success(result, serializer=PostSerializer)


@post.route('/', methods=['POST'])
def create():
    """Create new post.

    :return dict:
    """
    reader = Storage()
    data = Request.dict()
    result = reader.save(**data)
    return Response.success(result, serializer=PostSerializer)


@post.route('/<post_id>', methods=['PUT'])
def update(post_id):
    """Update concrete post.

    :param str post_id:
    :return dict:
    """
    reader = Storage()
    data = Request.dict()

    try:
        result = reader.update(post_id, **data)
    except NotExistsException:
        raise NotFound()

    return Response.success(result, serializer=PostSerializer)


@post.route('/<post_id>', methods=['DELETE'])
def delete(post_id):
    """Delete concrete post.

    :param str post_id:
    :return dict:
    """
    reader = Storage()

    try:
        reader.delete(post_id)
    except NotExistsException:
        raise NotFound()

    return Response.success({'success': True})


@post.route('/', methods=['PUT'])
def bulk_update():
    """Bulk update.

    :return list:
    """
    raise NotImplementedError("Bulk update")


@post.route('/', methods=['DELETE'])
def bulk_delete():
    """Bulk delete.

    :return list:
    """
    raise NotImplementedError("Bulk delete")

# -*- coding: utf-8 -*-
__author__ = 'boonya'

import json
from app import app
from app.models.post import Post
from app.utils.request import Request
from app.utils.response import Response
from app.reasons import errors
from app.utils.fs.exception import NotExistsException
from app.utils.fs import Fs
from app.models.post import PostSerializer


@app.route('/post', methods=['GET'])
def listing():
    """Get listing.

    :return list:
    """
    post = Post(Fs.get())

    try:
        posts = post.list()
    except Exception:
        return Response.failure(errors.UNKNOWN, 500)

    return Response.success(json.dumps(posts))


@app.route('/post/<post_id>', methods=['GET'])
def get(post_id):
    """Get concrete post.

    :param str post_id:
    :return dict:
    """
    fs = Fs.get()
    post = Post(fs)

    try:
        response = post.read(post_id)
    except NotExistsException:
        return Response.failure(errors.DOES_NOT_EXIST, 404)
    except Exception:
        return Response.failure(errors.UNKNOWN, 500)

    return Response.success(json.dumps(response, cls=PostSerializer))


@app.route('/post', methods=['POST'])
def create():
    """Create new post.

    :return dict:
    """
    post = Post(Fs.get())

    try:
        response = post.save(**Request.dict())
    except Exception:
        return Response.failure(errors.UNKNOWN, 500)

    return Response.success(json.dumps(response, cls=PostSerializer))


@app.route('/post/<post_id>', methods=['PUT'])
def update(post_id):
    """Update concrete post.

    :param str post_id:
    :return dict:
    """
    post = Post(Fs.get())

    try:
        response = post.update(post_id, **Request.dict())
    except NotExistsException:
        return Response.failure(errors.DOES_NOT_EXIST, 404)
    except Exception:
        return Response.failure(errors.UNKNOWN, 500)

    return Response.success(json.dumps(response, cls=PostSerializer))


@app.route('/post/<post_id>', methods=['DELETE'])
def delete(post_id):
    """Delete concrete post.

    :param str post_id:
    :return dict:
    """
    post = Post(Fs.get())

    try:
        response = post.delete(post_id)
    except NotExistsException:
        return Response.failure(errors.DOES_NOT_EXIST, 404)
    except Exception:
        return Response.failure(errors.UNKNOWN, 500)

    return Response.success(json.dumps(response, cls=PostSerializer))


@app.route('/post', methods=['PUT'])
def bulk_update():
    """Bulk update.

    :return list:
    """
    return Response.success(json.dumps("Bulk update"))


@app.route('/post', methods=['DELETE'])
def bulk_delete():
    """Bulk delete.

    :return list:
    """
    return Response.success(json.dumps("Bulk delete"))

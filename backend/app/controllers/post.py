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
    ---
    tags:
        - post
    responses:
        200:
            description: Posts listing.
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
    ---
    tags:
        - post
    parameters:
        -   name: post_id
            in: path
            description: ID of post
            required: true
            type: string
    responses:
        200:
            description: Posts listing.
            schema:
                type: object
                $ref: '#/definitions/PostModel'

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
    ---
    tags:
        - post
    parameters:
        -   name: category
            in: formData
            type: string
            required: true
        -   name: permalink
            in: formData
            type: string
            required: true
        -   name: layout
            in: formData
            type: string
            required: true
        -   name: language
            in: formData
            type: string
            required: true
        -   name: title
            in: formData
            type: string
            required: true
        -   name: cat_slug
            in: formData
            type: string
            required: true
        -   name: featured
            in: formData
            type: boolean
            required: true
        -   name: date
            in: formData
            type: string
            format: date-time
            required: true
        -   name: slug
            in: formData
            type: string
            required: true
        -   name: body
            in: formData
            type: string
            required: true

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
    ---
    tags:
        - post
    parameters:
        -   name: post_id
            in: path
            type: string
            required: true
        -   name: category
            in: formData
            type: string
        -   name: permalink
            in: formData
            type: string
        -   name: layout
            in: formData
            type: string
        -   name: language
            in: formData
            type: string
        -   name: title
            in: formData
            type: string
        -   name: cat_slug
            in: formData
            type: string
        -   name: featured
            in: formData
            type: boolean
        -   name: date
            in: formData
            type: string
            format: date-time
        -   name: slug
            in: formData
            type: string
        -   name: body
            in: formData
            type: string

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
    ---
    tags:
        - post
    parameters:
        -   name: post_id
            in: path
            type: string
            required: true

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
    ---
    tags:
        - post

    :return list:
    """
    return Response.success(json.dumps("Bulk update"))


@app.route('/post', methods=['DELETE'])
def bulk_delete():
    """Bulk delete.
    ---
    tags:
        - post

    :return list:
    """
    return Response.success(json.dumps("Bulk delete"))

__author__ = 'boonya'
import json
from app import app
from app.models.post import Post
from flask import request
from app.utils.response import Response
from app.reasons import errors
from app.utils.fs.exception import NotExistsException


@app.route('/post', methods=['GET'])
def listing():
    """Get listing.

    :return:
    """
    post = Post()
    posts = post.list()

    return Response.success(json.dumps(posts))


@app.route('/post/<post_id>', methods=['GET'])
def get(post_id):
    """Get concrete post.

    :param str post_id:
    :return:
    """
    post = Post()

    try:
        post = post.read(post_id)
    except NotExistsException:
        return Response.failure(errors.DOES_NOT_EXIST, 404)

    return Response.success(json.dumps(post))


@app.route('/post', methods=['POST'])
def create():
    """Create new post.

    :return:
    """
    return Response.success(json.dumps("Create post.\n"))


@app.route('/post/<post_id>', methods=['PUT'])
def update(post_id):
    """Update concrete post.

    :param str post_id:
    :return:
    """
    return Response.success(json.dumps("Update post: %s.\n" % post_id))


@app.route('/post/<post_id>', methods=['DELETE'])
def delete(post_id):
    """Delete concrete post.

    :param str post_id:
    :return:
    """
    return Response.success(json.dumps("Delete post: %s.\n" % post_id))


@app.route('/post', methods=['PUT'])
def bulk_update():
    """Bulk update.

    :return:
    """
    return Response.success(json.dumps("Bulk update"))


@app.route('/post', methods=['DELETE'])
def bulk_delete():
    """Bulk delete.

    :return:
    """
    return Response.success(json.dumps("Bulk delete"))

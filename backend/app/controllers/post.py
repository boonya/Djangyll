__author__ = 'boonya'
import json
from app import app
from app.models.post import Post
from app.utils.response import Response
from app.reasons import errors
from app.utils.fs.exception import NotExistsException


@app.route('/post', methods=['GET'])
def listing():
    post = Post()
    posts = post.list()

    return Response.success(json.dumps(posts))


@app.route('/post/<post_id>', methods=['GET'])
def get(post_id):
    post = Post()

    try:
        post = post.read(post_id)
    except NotExistsException:
        return Response.failure(errors.DOES_NOT_EXIST, 404)

    return Response.success(json.dumps(post))


@app.route('/post', methods=['POST'])
def create():
    return "Create post"


@app.route('/post<post_id>', methods=['PUT'])
def update(post_id):
    return "Update post: %s.\n" % post_id


@app.route('/post/<post_id>', methods=['DELETE'])
def delete(post_id):
    return "Delete post: %s.\n" % post_id


@app.route('/post', methods=['PUT'])
def bulk_update():
    return "Bulk update"


@app.route('/post', methods=['DELETE'])
def bulk_delete():
    return "Bulk delete"

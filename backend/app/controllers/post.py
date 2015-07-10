__author__ = 'boonya'
from app import app


@app.route('/post', methods=['GET'])
def listing():
    return "Listing of posts"


@app.route('/post/<post_id>', methods=['GET'])
def get(post_id):
    return "Get concrete post: %s.\n" % post_id


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

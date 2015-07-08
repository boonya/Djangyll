__author__ = 'boonya'

from flask import Flask


def __version__():
    from pkg_resources import get_distribution

    return get_distribution('djangyll').version


app = Flask(__name__, static_url_path="")

# Import all available routes from routes sub module
from controllers import post

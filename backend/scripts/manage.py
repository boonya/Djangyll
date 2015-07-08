"""

Usage:
    djangyll init [<CONFIG_FILE>]
    djangyll (start | stop | restart)
    djangyll start -t

Options:
    --nodaemon -t  Start as no daemon

"""
from flask import Flask
from docopt import docopt

app = Flask('Djangyll')


def start():
    app.run()


def main():
    args = docopt(__doc__)
    if args['start']:
        start()


if __name__ == '__main__':
    main()

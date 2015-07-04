from os import listdir
from os.path import isfile, join, isdir, exists
from utils.file_systems.interface import FileSystemInterface, NotExistsException


class Direct(FileSystemInterface):
    container = None

    def __init__(self, container):
        """Constructor.

        :param string container:
        :return:
        """
        if not isdir(container) or not exists(container):
            raise ValueError("'%s' is not a directory or does not exist." % container)

        self.container = container.rstrip('/')

    def list(self):
        return [f for f in listdir(self.container) if isfile(join(self.container, f))]

    def read(self, name):
        file_path = self.container + '/' + name

        if not exists(file_path) or not isfile(file_path):
            raise NotExistsException("'%s' is unknown file." % name)

        fh = open(file_path, 'r')
        data = fh.read()
        fh.close()
        return data

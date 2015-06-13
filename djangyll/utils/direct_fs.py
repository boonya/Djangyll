from utils.file_system import FileSystemInterface
from os import listdir
from os.path import isfile, join, isdir, exists


class DirectFs(FileSystemInterface):
    container = None

    def __init__(self, container):
        """
        Constructor.
        :param string container:
        :return:
        """
        if not isdir(container) or not exists(container):
            raise ValueError("'%s' is not a directory or does not exist." % container)

        self.container = container.rstrip('/')

    def list(self):
        return [f for f in listdir(self.container) if isfile(join(self.container, f))]

    def read(self, name):
        fh = open(self.container + '/' + name, 'r')
        data = fh.read()
        fh.close()
        return data

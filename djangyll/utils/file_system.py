class FileSystemInterface(object):
    def list(self):
        pass

    def read(self, path):
        pass

    def write(self, path, data):
        pass

    def copy(self, source, destination):
        pass

    def move(self, source, destination):
        pass

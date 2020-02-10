import os


class OSProxy():
    def exist_path(self, path):
        return os.path.exists(path)

    def create_directory(self, path):
        os.mkdir(path)

    def remove_directory(self, path):
        os.removedirs(path)

    def retrieve_files_from_directory(self, path):
        return os.scandir(path)

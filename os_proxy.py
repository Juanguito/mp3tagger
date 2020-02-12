import os
import shutil

class OSProxy():
    def exist_path(self, path):
        return os.path.exists(path)

    def create_directory(self, path):
        os.mkdir(path)

    def remove_file(self, path):
        os.remove(path)

    def remove_directory(self, path):
        shutil.rmtree(path)

    def retrieve_files_from_directory(self, path):
        return os.scandir(path)

    def join_paths(self, path_1, path_2):
        return os.path.join(path_1, path_2)

    def move_file(self, source, destination):
        os.rename(source, destination)
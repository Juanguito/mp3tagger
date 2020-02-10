import os
from os_proxy import OSProxy

class FolderManager():
    DIRECTORY_NAME = 'Awesome Mix Vol.'
    DIRECTORY_NUMBER = 1
    FILES_IN_DIRECTORY = 1
    MAX_FILES_IN_DIRECTORY = 149

    def __init__(self):
        self.proxy = OSProxy()

    def get_current_saving_directory(self):
        path = '{} {}'.format(self.DIRECTORY_NAME, self.DIRECTORY_NUMBER)

        if (
            self.proxy.exist_path(path) and
            self.FILES_IN_DIRECTORY < self.MAX_FILES_IN_DIRECTORY
        ):
            pass
        else:
            if (
                self.proxy.exist_path(path) and
                self.FILES_IN_DIRECTORY >= self.MAX_FILES_IN_DIRECTORY
            ):
                self.DIRECTORY_NUMBER += 1

            path = '{} {}'.format(self.DIRECTORY_NAME, self.DIRECTORY_NUMBER)
            self.proxy.create_directory(path)

        return path

    def retrieve_directory_files(self, path):
        with self.proxy.retrieve_files_from_directory(path) as entries:
            return tuple(entry for entry in entries if entry.is_file())

    def save_file_to_folder(self, file, path):
        pass

    def lele(self):
        completeName = os.path.join(path, file.name)

        with open(completeName, 'a') as output:
            output.write(file)

        return True

####################################
    def retrieve_files(self, path):
        #1
        # return list(os.scandir(path))

        #2
        #return tuple(entry for entry in os.scandir(path) if entry.is_file())

        #3
        with os.scandir(path) as entries:
            return tuple(entry for entry in entries if entry.is_file())

    def save_file(self):
        pass

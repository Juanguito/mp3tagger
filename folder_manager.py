from os_proxy import OSProxy

class FolderManager():
    DIRECTORY_NAME = 'Awesome Mix Vol.'
    DIRECTORY_NUMBER = 1
    FILES_IN_DIRECTORY = 1
    MAX_FILES_IN_DIRECTORY = 149

    def __init__(self):
        self.path_proxy = OSProxy()

    def exist_path(self, path):
        return self.path_proxy.exist_path(path)

    def remove_file(self, path):
        self.path_proxy.remove_file(path)

    def get_current_saving_directory(self):
        path = '{} {}'.format(self.DIRECTORY_NAME, self.DIRECTORY_NUMBER)

        if (
            self.path_proxy.exist_path(path) and
            self.FILES_IN_DIRECTORY < self.MAX_FILES_IN_DIRECTORY
        ):
            pass
        else:
            if (
                self.path_proxy.exist_path(path) and
                self.FILES_IN_DIRECTORY >= self.MAX_FILES_IN_DIRECTORY
            ):
                self.DIRECTORY_NUMBER += 1

            path = '{} {}'.format(self.DIRECTORY_NAME, self.DIRECTORY_NUMBER)
            self.path_proxy.create_directory(path)

        return path

    def retrieve_directory_files(self, path):
        with self.path_proxy.retrieve_files_from_directory(path) as entries:
            return tuple(
                entry for entry in entries
                if entry.is_file() and entry.name.endswith('.mp3')
            )

    def save_file_to_folder(self, file, path):
        pass

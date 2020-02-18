from folder_manager import FolderManager
from os_proxy import OSProxy
from unittest import TestCase
from unittest.mock import Mock


class TestFileManager(TestCase):
    os_proxy = OSProxy()
    source_path = '/files'
    source_within_directory_path = '/files/folder'

    def setUp(self):
        self.manager = FolderManager()
        self.destination_path = 'Awesome Mix Vol. 1'
        self.destination_path_when_full = 'Awesome Mix Vol. 2'

        if self.os_proxy.exist_path(self.destination_path):
            self.os_proxy.remove_directory(self.destination_path)

        if self.os_proxy.exist_path(self.destination_path_when_full):
            self.os_proxy.remove_directory(
                self.destination_path_when_full
        )

        if self.os_proxy.exist_path(self.source_path):
            self.os_proxy.remove_directory(self.source_path)

    def test_get_new_saving_directory(self):
        saving_directory = self.manager.get_current_saving_directory()

        assert saving_directory == self.destination_path

    def test_get_saving_directory_when_it_exists_and_not_full(self):
        self.os_proxy.create_directory(self.destination_path)

        saving_directory = self.manager.get_current_saving_directory()

        assert saving_directory == self.destination_path

    def test_get_saving_directory_when_it_exists_and_is_full(self):
        self.os_proxy.create_directory(self.destination_path)

        self.manager.FILES_IN_DIRECTORY = self.manager.MAX_FILES_IN_DIRECTORY

        saving_directory = self.manager.get_current_saving_directory()

        assert saving_directory == self.destination_path_when_full

    def test_retrieve_only_files_from_not_existing_directory(self):
        with self.assertRaises(FileNotFoundError):
            self.manager.retrieve_directory_files(
                self.source_path
            )

    def test_retrieve_only_files_from_existing_directory(self):
        self.os_proxy.create_directory(self.source_path)
        self.os_proxy.create_directory(self.source_within_directory_path)

        completeName = self.os_proxy.join_paths(self.source_path, "test.mp3")
        with open(completeName, "w") as file:
            file.write(' ')

        entries = self.manager.retrieve_directory_files(
            self.source_path
        )

        assert len(entries) == 1

    def test_retrieve_only_mp3_files_from_existing_directory(self):
        self.os_proxy.create_directory(self.source_path)
        self.os_proxy.create_directory(self.source_within_directory_path)

        completeName = self.os_proxy.join_paths(self.source_path, "test.mp3")
        with open(completeName, "w") as file:
            file.write(' ')

        completeName2 = self.os_proxy.join_paths(self.source_path, "test.txt")
        with open(completeName2, "w") as file:
            file.write(' ')

        entries = self.manager.retrieve_directory_files(
            self.source_path
        )

        assert len(entries) == 1

    def test_save_file_to_other_folder(self):
        pass
        # source_file = os.DirEntry()
        # source_file.name = '/test/test.mp3'

        # assert open(completeName, "r")

    def test_path_not_exist(self):
        assert not self.manager.exist_path(self.source_path)

    def test_path_exist(self):
        self.os_proxy.create_directory(self.source_path)

        assert self.manager.exist_path(self.source_path)

    def test_remove_not_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            self.manager.remove_file(self.source_path)

    def test_remove_existing_file(self):
        with open(self.source_path, "w") as file:
            file.write(' ')

        self.manager.remove_file(self.source_path)

        assert not self.manager.exist_path(self.source_path)

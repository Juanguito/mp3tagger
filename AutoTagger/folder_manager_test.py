from folder_manager import FolderManager
import shutil
from unittest import TestCase
import os


class TestFileManager(TestCase):
    def setUp(self):
        self.manager = FolderManager()
        self.destination_path = 'Awesome Mix Vol. 1'
        self.destination_path_when_full = 'Awesome Mix Vol. 2'

        if os.path.exists(self.destination_path):
            shutil.rmtree(self.destination_path, ignore_errors=True)

        if os.path.exists(self.destination_path_when_full):
            shutil.rmtree(
                self.destination_path_when_full,
                ignore_errors=True
        )

        self.source_path = '/files'
        self.source_within_directory_path = '/files/folder'

        if os.path.exists(self.source_path):
            shutil.rmtree(self.source_path, ignore_errors=True)

    def test_get_new_saving_directory(self):
        saving_directory = self.manager.get_current_saving_directory()

        assert saving_directory == self.destination_path

    def test_get_saving_directory_when_it_exists_and_not_full(self):
        os.mkdir(self.destination_path)

        saving_directory = self.manager.get_current_saving_directory()

        assert saving_directory == self.destination_path

    def test_get_saving_directory_when_it_exists_and_is_full(self):
        os.mkdir(self.destination_path)

        self.manager.FILES_IN_DIRECTORY = self.manager.MAX_FILES_IN_DIRECTORY

        saving_directory = self.manager.get_current_saving_directory()

        assert saving_directory == self.destination_path_when_full

    def test_retrieve_only_files_from_existing_directory(self):
        os.mkdir(self.source_path)
        os.mkdir(self.source_within_directory_path)

        completeName = os.path.join(self.source_path, "test.mp3")         
        with open(completeName, "w") as file:
            file.write(' ')

        entries = self.manager.retrieve_directory_files(
            self.source_path
        )

        assert len(entries) == 1

    def test_save_file_to_other_folder(self):
        source_file = os.DirEntry()
        source_file.name = '/test/test.mp3'

        assert open(completeName, "r")

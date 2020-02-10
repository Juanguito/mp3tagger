import os
import shutil
from unittest import TestCase
from os_proxy import OSProxy


class TestPathProxy(TestCase):
    def setUp(self):
        self.files_path = './files'
        self.wrong_path = './lele'

        if os.path.exists(self.files_path):
            shutil.rmtree(self.files_path, ignore_errors=True)

    def test_instantiate_path_proxy_class(self):
        assert OSProxy()

    def test_given_directory_not_exist(self):
        path_proxy = OSProxy()
        assert not path_proxy.exist_path(self.wrong_path)

    def test_given_directory_exist(self):
        os.mkdir(self.files_path)

        path_proxy = OSProxy()
        assert path_proxy.exist_path(self.files_path)

    def test_create_directory(self):
        path_proxy = OSProxy()
        path_proxy.create_directory(self.files_path)

        assert os.path.exists(self.files_path)

    def test_create_existing_directory(self):
        os.mkdir(self.files_path)

        path_proxy = OSProxy()
        with self.assertRaises(FileExistsError):
            path_proxy.create_directory(self.files_path)

    def test_remove_existing_directory(self):
        os.mkdir(self.files_path)

        path_proxy = OSProxy()
        path_proxy.remove_directory(self.files_path)

        assert not os.path.exists(self.files_path)

    def test_remove_not_existing_directory(self):
        path_proxy = OSProxy()

        with self.assertRaises(FileNotFoundError):
            path_proxy.remove_directory(self.files_path)

    def test_retrieve_files_from_not_existing_directory(self):
        path_proxy = OSProxy()

        with self.assertRaises(FileNotFoundError):
            path_proxy.retrieve_files_from_directory(self.files_path)

    def test_retrieve_files_from_directory(self):
        path_proxy = OSProxy()
        os.mkdir(self.files_path)
        completeName = os.path.join(self.files_path, "test.mp3")         
        with open(completeName, "w") as file:
            file.write(' ')

        entries = path_proxy.retrieve_files_from_directory(self.files_path)
        files = tuple(entry for entry in entries if entry.is_file())

        assert len(files) == 1

    def test_remove_not_existing_file(self):
        
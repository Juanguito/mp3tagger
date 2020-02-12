import os
import shutil
from unittest import TestCase
from unittest.mock import Mock
from os_proxy import OSProxy


class TestPathProxy(TestCase):

    path_proxy = OSProxy()

    def setUp(self):
        self.files_path = './files'
        self.wrong_path = './lele'
        self.file_name = 'test.mp3'
        self.other_file_name = 'other.mp3'

        if os.path.exists(self.files_path):
            shutil.rmtree(self.files_path, ignore_errors=True)

    def test_instantiate_path_proxy_class(self):
        assert OSProxy()

    def test_given_directory_not_exist(self):
        assert not self.path_proxy.exist_path(self.wrong_path)

    def test_given_directory_exist(self):
        os.mkdir(self.files_path)

        assert self.path_proxy.exist_path(self.files_path)

    def test_create_directory(self):
        self.path_proxy.create_directory(self.files_path)
        assert os.path.exists(self.files_path)

    def test_create_existing_directory(self):
        os.mkdir(self.files_path)

        with self.assertRaises(FileExistsError):
            self.path_proxy.create_directory(self.files_path)

    def test_remove_existing_directory(self):
        os.mkdir(self.files_path)

        self.path_proxy.remove_directory(self.files_path)

        assert not os.path.exists(self.files_path)

    def test_remove_not_existing_directory(self):
        with self.assertRaises(FileNotFoundError):
            self.path_proxy.remove_directory(self.files_path)

    def test_retrieve_files_from_not_existing_directory(self):
        with self.assertRaises(FileNotFoundError):
            self.path_proxy.retrieve_files_from_directory(self.files_path)

    def test_retrieve_files_from_directory(self):
        os.mkdir(self.files_path)
        completeName = os.path.join(self.files_path, self.file_name)
        with open(completeName, "w") as file:
            file.write(' ')

        entries = self.path_proxy.retrieve_files_from_directory(self.files_path)
        files = tuple(entry for entry in entries if entry.is_file())

        assert len(files) == 1

    def test_join_path_with_some_none(self):
        with self.assertRaises(TypeError):
            self.path_proxy.join_paths(None, None)

        with self.assertRaises(TypeError):
            self.path_proxy.join_paths(self.files_path, None)

        with self.assertRaises(TypeError):
            self.path_proxy.join_paths(None, self.file_name)

    def test_join_path_ok(self):
        assert self.path_proxy.join_paths(
            self.files_path,
            self.file_name
        ) == './files\\test.mp3'

    def test_try_to_remove_path_None(self):
        with self.assertRaises(TypeError):
            self.path_proxy.remove_file(None)

    def test_remove_not_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            self.path_proxy.remove_file(self.file_name)

    def test_remove_file(self):
        with open(self.file_name, "w") as file:
            file.write(' ')

        self.path_proxy.remove_file(self.file_name)

    def test_move_file_to_none_path(self):
        with self.assertRaises(TypeError):
            self.path_proxy.move_file(None, None)

        with self.assertRaises(TypeError):
            self.path_proxy.move_file(self.file_name, None)

        with self.assertRaises(TypeError):
            self.path_proxy.move_file(None, self.other_file_name)

    def test_move_file_to_not_existing_path(self):
        with self.assertRaises(TypeError):
            self.path_proxy.move_file(self.file_name, None)

    def test_move_file_to_none_path(self):
        wrong_path = self.path_proxy.join_paths(self.wrong_path, self.other_file_name)
        self.path_proxy.move_file(self.file_name, wrong_path)

        assert self.path_proxy.exist_path('./lele/other.mp3')


from unittest import TestCase
from unittest.mock import MagicMock
from tag_manager import TagManager
from folder_manager import FolderManager

class TestTagManager(TestCase):
    wrong_path = 'wrong.mp3'
    not_mp3_file_path = 'file.txt'

    def setUp(self):
        self.tag_manager = TagManager()
        self.folder_manager = FolderManager()

        if self.folder_manager.exist_path(self.not_mp3_file_path):
            self.folder_manager.remove_file(self.not_mp3_file_path)

    def test_instantiate_tag_manager(self):
        assert TagManager()

    def test_retrieve_file_from_none_path(self):
        with self.assertRaises(FileNotFoundError):
            self.tag_manager.mp3_file(self.wrong_path)

    def test_retrieve_not_mp3_file(self):
        with open(self.not_mp3_file_path, 'w') as file:
            file.write(' ')

        with self.assertRaises(FileNotFoundError):
            self.tag_manager.mp3_file(self.not_mp3_file_path)

    # def test_retrieve_mp3_file(self):

    def test_retrieve_tags_from_mp3(self):
        
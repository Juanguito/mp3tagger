from unittest import TestCase, mock
from tag_proxy import TagProxy
from os_proxy import OSProxy

class TestFileProxy(TestCase):

    mp3_file_path = 'test.mp3'
    not_mp3_file_path = 'test.txt'
    destination_path = './test'
    artist = 'Blur'
    song = 'Song 2'
    os_proxy = OSProxy()

    def setUp(self):
        self.tag_proxy = TagProxy()

        if self.os_proxy.exist_path(self.mp3_file_path):
            self.os_proxy.remove(self.mp3_file_path)

    def test_instantiate_file_proxy(self):
        assert TagProxy()
    
    def test_open_not_existing_file_from_path(self):
        with self.assertRaises(FileNotFoundError):
            self.tag_proxy.retrieve_mp3_file(self.mp3_file_path)

    def test_return_mp3_file_from_path(self):
        with open(self.mp3_file_path, 'w') as file:
            file.write(' ')

        mp3file = self.tag_proxy.retrieve_mp3_file(self.mp3_file_path)

        assert mp3file

    def test_read_V1_tags_from_None(self):
        with self.assertRaises(AttributeError):
            self.tag_proxy.read_v1_tags(None)

    def test_read_V1_tags_from_not_mp3_file(self):
        file = mock.Mock(spec_set=True)

        with self.assertRaises(AttributeError):
            self.tag_proxy.read_v1_tags(file)

    def test_read_V1_tags_from_mp3_file(self):
        file = mock.Mock(artist= self.artist, song= self.song)

        tags = self.tag_proxy.read_v1_tags(file)

        assert tags['artist'] ==  self.artist
        assert tags['song'] ==  self.song

    def test_write_V1_tags_to_None(self):
        with self.assertRaises(AttributeError):
            self.tag_proxy.write_v1_tags(None, {})

    def test_write_V1_tags_from_not_mp3_file(self):
        file = mock.Mock(spec_set=True)

        with self.assertRaises(AttributeError):
            self.tag_proxy.write_v1_tags(file, {})

    def test_write_V1_tags_from_mp3_file(self):
        tags = {
            'artist': self.artist,
            'song': self.song,
        }
        file = mock.Mock()

        self.tag_proxy.write_v1_tags(file, tags)

        assert file.artist ==  self.artist
        assert file.song == self.song

    def test_read_V2_tags_from_None(self):
        with self.assertRaises(AttributeError):
            self.tag_proxy.read_v2_tags(None)

    def test_read_V2_tags_from_not_mp3_file(self):
        file = mock.Mock(spec_set=True)

        with self.assertRaises(AttributeError):
            self.tag_proxy.read_v2_tags(file)

    def test_read_V2_tags_from_mp3_file(self):
        file = mock.Mock(artist= self.artist, song= self.song)

        tags = self.tag_proxy.read_v2_tags(file)

        assert tags['artist'] ==  self.artist
        assert tags['song'] ==  self.song

    def test_write_V2_tags_to_None(self):
        with self.assertRaises(AttributeError):
            self.tag_proxy.write_v2_tags(None, {})

    def test_write_V2_tags_from_not_mp3_file(self):
        file = mock.Mock(spec_set=True)

        with self.assertRaises(AttributeError):
            self.tag_proxy.write_v2_tags(file, {})

    def test_write_V2_tags_from_mp3_file(self):
        tags = {
            'artist': self.artist,
            'song': self.song,
        }
        file = mock.Mock()

        self.tag_proxy.write_v2_tags(file, tags)

        assert file.artist ==  self.artist
        assert file.song == self.song




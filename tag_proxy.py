from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

class TagProxy():
    def retrieve_mp3_file(self, path):
        return MP3File(path)

    def read_v1_tags(self, file):
        file.set_version(VERSION_1)

        return {
            'artist': file.artist,
            'song': file.song,
        }

    def write_v1_tags(self, file, tags):
        file.set_version(VERSION_1)

        file.artist = tags['artist']
        file.song = tags['song']

        file.save()

    def read_v2_tags(self, file):
        file.set_version(VERSION_2)

        return {
            'artist': file.artist,
            'song': file.song,
        }

    def write_v2_tags(self, file, tags):
        file.set_version(VERSION_2)

        file.artist = tags['artist']
        file.song = tags['song']

        file.save()

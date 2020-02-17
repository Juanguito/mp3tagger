from tag_proxy import TagProxy


class TagManager():
    def __init__(self):
        self.tag_manager = TagProxy()

    def mp3_file(self, path):
        return self.tag_manager.retrieve_mp3_file(path)

from folder_manager import FolderManager
from tag_manager import TagManager

def main():
    print("python main function")

    folder_manager = FolderManager()
    tag_manager = TagManager()

    entries = folder_manager.retrieve_directory_files('./files')

    for entry in entries:
        mp3_file = tag_manager.mp3_file(entry.name)
        



if __name__ == '__main__':
    main()

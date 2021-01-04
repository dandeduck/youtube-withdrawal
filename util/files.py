class File:
    def directory(self) -> str:
        pass

    def name(self) -> str:
        pass

    def extension(self) -> str:
        pass

    def path(self):
        return self.directory() + self.name() + self.extension()


class FileBase(File):
    directory = ''
    name = ''
    extension = ''

    def __init__(self, directory, name, extension):
        self.directory = directory
        self.name = name
        self.extension = extension

    def directory(self) -> str:
        return self.directory

    def name(self) -> str:
        return self.name

    def extension(self) -> str:
        return self.extension


class AudioFile(FileBase):
    def __init__(self, directory, name):
        super().__init__(directory, name, '.mp3')


class VideoFile(FileBase):
    def __init__(self, directory, name):
        super().__init__(directory, name, '.mp4')
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
    directoryStr = ''
    nameStr = ''
    extensionStr = ''

    def __init__(self, directory, name, extension):
        self.directoryStr = directory
        self.nameStr = name
        self.extensionStr = extension

    def directory(self) -> str:
        return self.directoryStr

    def name(self) -> str:
        return self.nameStr

    def extension(self) -> str:
        return self.extensionStr


class AudioFile(FileBase):
    def __init__(self, directory, name):
        super().__init__(directory, name, '.mp3')


class VideoFile(FileBase):
    def __init__(self, directory, name):
        super().__init__(directory, name, '.mp4')
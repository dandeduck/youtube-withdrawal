import pafy
import ffmpeg

from files import VideoFile, AudioFile


class VideoSettings:
    cacheDir = ''
    outputDir = ''
    resolution = ''

    def __init__(self, cacheDir, outputDir, resolution):
        self.cacheDir = cacheDir
        self.outputDir = outputDir
        self.resolution = resolution


class Video:
    video = None
    videoFile = None
    audioFile = None
    outputFile = None
    resolution = ''

    def __init__(self, videoId, settings):
        self.video = pafy.new(videoId)
        self.videoFile = VideoFile(settings.cacheDir, self.video.title)
        self.audioFile = AudioFile(settings.cacheDir, self.video.title)
        self.outputFile = VideoFile(settings.outputDir, self.video.title)
        self.resolution = settings.resolution

    def downloadFiles(self):
        self.__closestResolutionStream().download(filepath=self.videoFile.path())
        self.video.getbestaudio().download(filepath=self.audioFile.path())

    def outputVideo(self):
        if not self.__fileExists(self.outputFile.path()):
            video = ffmpeg.input(self.videoFile.path()).video
            audio = ffmpeg.input(self.audioFile.path()).audio
            ffmpeg.concat(video, audio, v=1, a=1).output(self.outputFile.path()).run()

    def __closestResolutionStream(self):
        for stream in self.video.videostreams:
            if stream.notes == self.resolution:
                return stream

        return self.video.getbestvideo()

    def __fileExists(self, filePath):
        try:
            file = open(filePath)
            file.close()
            return True
        except IOError:
            return False



class VideoCollection:
    settings = None
    videos = []

    def __init__(self, settings, videoIds):
        self.settings = settings
        self.generateVideos(videoIds)

    def generateVideos(self, videoIds):
        for videoId in videoIds:
            self.videos.append(Video(videoId, self.settings))

    def downloadVideos(self):
        for video in self.videos:
            video.download()

    def outputVideos(self):
        for video in self.videos:
            video.outputVideo()

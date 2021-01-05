import pafy
import moviepy.editor as mpe

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

    def downloadVideos(self):
        self.__closestResolutionStream().download(filepath=self.videoFile.path())
        self.video.getbestaudio().download(filepath=self.audioFile.path())

    def __closestResolutionStream(self):
        for stream in self.video.videostreams:
            if stream.notes == self.resolution:
                return stream

        return self.video.getbestvideo()

    def outputVideo(self):
        videoClip = mpe.VideoFileClip(self.videoFile.path())
        audioClip = mpe.AudioFileClip(self.audioFile.path())
        mergedClip = videoClip.set_audio(audioClip)
        mergedClip.write_videofile(self.outputFile.path(), fps=videoClip.fps)


class VideoGenerator:
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
            video.downloadVideos()

    def outputVideos(self):
        for video in self.videos:
            try:
                video.outputVideo()
            except Exception as e:
                continue #will be logged inthe future

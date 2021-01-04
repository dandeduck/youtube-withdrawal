import pafy
import moviepy.editor as mpe

from files import VideoFile, AudioFile
from util import resToPixels


class Video:
    video = None
    videoFile = None
    audioFile = None
    outputFile = None
    maxPixels = 0

    def __init__(self, videoId, cacheDir, outputDir, resolution):
        self.video = pafy.new(videoId)
        self.videoFile = VideoFile(cacheDir, self.video.title)
        self.audioFile = AudioFile(cacheDir, self.video.title)
        self.outputFile = VideoFile(outputDir, self.video.title)
        self.maxPixels = resToPixels(resolution)

    def downloadVideos(self):
        selectedStream = None
        if self.__videoPixels(self.video.getbestvideo()) <= self.maxPixels:
            selectedStream = self.video.getbestvideo()
        else:
            for stream in self.video.videostreams:
                if self.__videoPixels(stream) >= self.maxPixels:
                    selectedStream = stream
                    break

        selectedStream.download(filepath=self.videoFile.path())
        self.video.getbestaudio().download(filepath=self.audioFile.path())

    @classmethod
    def __videoPixels(cls, stream):
        dimensions = stream.resolution.split('x')
        return int(dimensions[0]) * int(dimensions[1])

    def mergeClips(self):
        videoClip = mpe.VideoFileClip(self.videoFile.path())
        audioClip = mpe.VideoFileClip(self.audioFile.path())
        mergedClip = videoClip.set_audio(audioClip)
        mergedClip.write_videofile(self.outputFile.path())

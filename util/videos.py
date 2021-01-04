import pafy
import moviepy.editor as mpe

from util.files import VideoFile, AudioFile


class Video:
    video = None
    videoFile = None
    audioFile = None
    outputFile = None
    maxResWidth = 0

    def __init__(self, videoId, cacheDir, outputDir, maxResWidth):
        self.video = pafy.new(videoId)
        self.videoFile = VideoFile(cacheDir, self.video.title())
        self.audioFile = AudioFile(cacheDir, self.video.title())
        self.outputFile = VideoFile(outputDir, self.video.title())
        self.maxResWidth = maxResWidth

    def downloadVideos(self):
        selectedStream = None
        if self.videoWidth(self.video.getbestvideo()) <= self.maxResWidth:
            selectedStream = self.video.getbestvideo()
        else:
            for stream in self.video.videostreams:
                if(self.videoWidth(stream) >= self.maxResWidth):
                    selectedStream = stream

        selectedStream.download(filepath=self.videoFile.path())
        self.video.getbestaudio().download(filepath=self.audioFile.path())

    @classmethod
    def videoWidth(cls, stream):
        return int(stream.resolution.split('x')[0])

    def mergeClips(self):
        videoClip = mpe.VideoFileClip(self.videoFile.path())
        audioClip = mpe.VideoFileClip(self.audioFile.path())
        mergedClip = videoClip.set_audio(audioClip)
        mergedClip.write_videofile(self.outputFile.path())

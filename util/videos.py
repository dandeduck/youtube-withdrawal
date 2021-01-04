import pafy
import moviepy.editor as mpe

from util.files import VideoFile, AudioFile


class Video:
    video = None
    videoFile = None
    audioFile = None
    outputFile = None

    def __init__(self, videoId, cacheDir, outputDir):
        self.video = pafy.new(videoId)
        self.videoFile = VideoFile(cacheDir, self.video.title())
        self.audioFile = AudioFile(cacheDir, self.video.title())
        self.outputFile = VideoFile(outputDir, self.video.title())

    def downloadVideos(self):
        self.video.getbestvideo().download(filepath=self.videoFile.path())
        self.video.getbestaudio().download(filepath=self.audioFile.path())

    def mergeClips(self):
        videoClip = mpe.VideoFileClip(self.videoFile.path())
        audioClip = mpe.VideoFileClip(self.audioFile.path())
        mergedClip = videoClip.set_audio(audioClip)
        mergedClip.write_videofile(self.outputFile.path())

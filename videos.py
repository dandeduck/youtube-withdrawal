import pafy
import moviepy.editor as mpe

from files import VideoFile, AudioFile


class Video:
    video = None
    videoFile = None
    audioFile = None
    outputFile = None
    resolution = ''

    def __init__(self, videoId, cacheDir, outputDir, resolution):
        self.video = pafy.new(videoId)
        self.videoFile = VideoFile(cacheDir, self.video.title)
        self.audioFile = AudioFile(cacheDir, self.video.title)
        self.outputFile = VideoFile(outputDir, self.video.title)
        self.resolution = resolution

    def downloadVideos(self):
        self.__closestResolutionStream().download(filepath=self.videoFile.path())
        self.video.getbestaudio().download(filepath=self.audioFile.path())

    def __closestResolutionStream(self):
        for stream in self.video.videostreams:
            if stream.notes == self.resolution:
                return stream

        return self.video.getbestvideo()

    def mergeClips(self):
        videoClip = mpe.VideoFileClip(self.videoFile.path())
        audioClip = mpe.AudioFileClip(self.audioFile.path())
        mergedClip = videoClip.set_audio(audioClip)
        mergedClip.write_videofile(self.outputFile.path(), fps=videoClip.fps)

import pafy
import moviepy.editor as mpe


def generateVideo(videoId, cacheDir, outputDir):
    video = pafy.new(videoId)
    cachePath = cacheDir + video.title()
    audioExtension = '.mp3'
    videoExtension = '.mp4'
    outputPath = outputDir + video.title() + videoExtension

    downloadVideos(video, cachePath, audioExtension, videoExtension)
    mergeClips(cachePath+videoExtension, cachePath+audioExtension, outputPath)


def downloadVideos(video, path, audioExtension, videoExtension):
    video.getbestaudio().download(filepath=path + audioExtension)
    video.getbestvideo().download(filepath=path + videoExtension)


def mergeClips(videoPath, audioPath, outputPath):
    videoClip = mpe.VideoFileClip(videoPath)
    audioClip = mpe.VideoFileClip(audioPath)
    mergedClip = videoClip.set_audio(audioClip)
    mergedClip.write_videofile(outputPath)

# if __name__ == '__main__':

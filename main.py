from videos import Video, VideoSettings

if __name__ == '__main__':
    video = Video("https://www.youtube.com/watch?v=0_RZby28s9E", VideoSettings('C:\\Users\\duck\\Documents\\test\\', 'C:\\Users\\duck\\Documents\\test\\output\\', '1080p60'))
    video.downloadVideos()
    video.outputVideo()

from videos import Video

if __name__ == '__main__':
    video = Video("https://www.youtube.com/watch?v=Y0muXSQRVEg&ab_channel=LinusTechTips", 'C:\\Users\\duck\\Documents\\test\\', 'C:\\Users\\duck\\Documents\\test\\output\\', '1080p')
    video.downloadVideos()
    video.mergeClips()

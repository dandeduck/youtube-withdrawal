from services import YoutubeApi

CLIENT_SECRETS_FILE = "C:\\Users\\duck\\Documents\\clientSecret.json"

if __name__ == '__main__':
    api = YoutubeApi(CLIENT_SECRETS_FILE)
    print(api.userSubscriptions())
    print(type(api.retrieveAllItems(api.userSubscriptions)[0]))
    # print(api.search(q='2b2t')['items'])


# from videos import Video, VideoSettings
#
# if __name__ == '__main__':
#     video = Video("https://www.youtube.com/watch?v=0_RZby28s9E", VideoSettings('C:\\Users\\duck\\Documents\\test\\', 'C:\\Users\\duck\\Documents\\test\\output\\', '1080p60'))
#     video.downloadVideos()
#     video.outputVideo()

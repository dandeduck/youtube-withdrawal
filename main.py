import services
import datetime

from storage import DataBase

CLIENT_SECRETS_FILE = "C:\\Users\\duck\\Documents\\clientSecret.json"

if __name__ == '__main__':
    # api = services.YoutubeApi(CLIENT_SECRETS_FILE)
    # checker = services.UploadChecker(api, ['UCXuqSBlHAE6Xw-yeJA0Tunw', 'UCtyjKSJa-3kMbCSjjOCLq2A'])
    # print(checker.newVideoIds(datetime.datetime(2021, 1, 1, 0, 0, 0, 0)))
    # # print(api.search(q='2b2t')['items'])
    # db = DataBase("db")
    # db.createLastCheckedDatetimeTable()
    # print("def " + str(db.lastCheckedTime()))
    # db.updateLastCheckedDatetime()
    # print("now " + str(db.lastCheckedTime()))


# from videos import Video, VideoSettings
#
# if __name__ == '__main__':
#     video = Video("https://www.youtube.com/watch?v=0_RZby28s9E", VideoSettings('C:\\Users\\duck\\Documents\\test\\', 'C:\\Users\\duck\\Documents\\test\\output\\', '1080p60'))
#     video.downloadVideos()
#     video.outputVideo()

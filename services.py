from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from videos import VideoCollection


class YoutubeApi:
    MIN_SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'

    service = None

    def __init__(self, clientSecretFile, scopes=None):
        if scopes is None:
            scopes = self.MIN_SCOPES
        self.service = self.__getAuthenticated_service(clientSecretFile, scopes)

    def playlistItems(self, **kwargs):
        kwargs['maxResults'] = 50

        return self.service.playlistItems().list(**kwargs).execute()

    def subscriptions(self, **kwargs):
        kwargs['maxResults'] = 50

        return self.service.subscriptions().list(**kwargs).execute()

    def retrieveAllItems(self, apiFunc, **kwargs):
        kwargs['maxResults'] = 50
        result = apiFunc(**kwargs)

        if 'nextPageToken' in result.keys():
            kwargs['pageToken'] = result['nextPageToken']
            return result['items'] + self.retrieveAllItems(apiFunc, **kwargs)

        return result['items']

    def __getAuthenticated_service(self, clientSecretFile, scopes):
        flow = InstalledAppFlow.from_client_secrets_file(clientSecretFile, scopes)
        credentials = flow.run_local_server()

        return build(self.API_SERVICE_NAME, self.API_VERSION, credentials=credentials)


class UploadChecker:
    api = None
    channelIds = []

    def __init__(self, youtubeApi, channelIds):
        self.api = youtubeApi
        self.channelIds = channelIds

    def newVideoIds(self, lastCheckedTimestamp): #1970-01-01T00:00:00Z
        ids = []

        for channelId in self.channelIds:
            ids += self.__newVideoIdsFromChannel(channelId, lastCheckedTimestamp)

        return ids

    def __newVideoIdsFromChannel(self, channelId, lastCheckedTimestamp):
        return [item['id']['videoId'] for item in
                self.api.search(part='snippet', channelId=channelId, publishedAfter=lastCheckedTimestamp, type='video',
                                maxResults=50)['items']]


class NewVideoCollectionFactory:
    settings = None
    uploadChecker = None

    def __init__(self, settings, uploadChecker):
        self.settings = settings
        self.uploadChecker = uploadChecker

    def createNewVideoCollection(self, lastCheckedTimestamp):
        return VideoCollection(self.settings, self.uploadChecker.newVideoIds(lastCheckedTimestamp))

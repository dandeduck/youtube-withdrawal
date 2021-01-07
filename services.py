import datetime

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from util import DateTimeParser
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
    playlistIds = []

    def __init__(self, youtubeApi, channelIds):
        self.api = youtubeApi
        self.playlistIds = [channelId.replace('C', 'U', 1) for channelId in channelIds.copy()]

        print(self.playlistIds)

    def newVideoIds(self, lastCheckedDatetime):
        ids = []

        for playlistId in self.playlistIds:
            ids += self.__newVideoIdsFromChannel(playlistId, lastCheckedDatetime)

        return ids

    def __newVideoIdsFromChannel(self, playlistId, lastCheckedDatetime):
        contentDetails = [item['contentDetails'] for item in self.api.playlistItems(part='contentDetails', playlistId=playlistId)['items']]
        newVideoIds = []

        for detail in contentDetails:
            publishTime = DateTimeParser.fromRFC3339(detail['videoPublishedAt'])

            if publishTime > lastCheckedDatetime:
                newVideoIds.append(detail['videoId'])
            else:
                break

        return newVideoIds


class NewVideoCollectionFactory:
    settings = None
    uploadChecker = None

    def __init__(self, settings, uploadChecker):
        self.settings = settings
        self.uploadChecker = uploadChecker

    def createNewVideoCollection(self, lastCheckedDatetime):
        return VideoCollection(self.settings, self.uploadChecker.newVideoIds(lastCheckedDatetime))

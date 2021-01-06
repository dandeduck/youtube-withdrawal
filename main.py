from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "C:\\Users\\duck\\Documents\\clientSecret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server()

    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


if __name__ == '__main__':
    service = get_authenticated_service()
    print(service.search().list(part='snippet', q='2b2t').execute())

# from videos import Video, VideoSettings
#
# if __name__ == '__main__':
#     video = Video("https://www.youtube.com/watch?v=0_RZby28s9E", VideoSettings('C:\\Users\\duck\\Documents\\test\\', 'C:\\Users\\duck\\Documents\\test\\output\\', '1080p60'))
#     video.downloadVideos()
#     video.outputVideo()

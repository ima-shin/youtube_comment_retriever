import csv
import os.path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from data import Settings


class Youtube(object):

    YOUTUBE = build(
        Settings.YOUTUBE_SERVICE_NAME.value,
        Settings.YOUTUBE_API_VERSION.value,
        developerKey=Settings.YOUTUBE_API_KEY.value
    )

    next_page_token = None

    def search(self, params):
        try:
            res = self.YOUTUBE.search().list(
                part=params.get("part"),
                order="date",
                channelId=params.get("channelId")
            ).execute()
        except HttpError as e:
            print(e)
            if e.status_code == 403:
                raise QuotaExceededException("Quota limits exceeded.")
            raise HttpError(e)
        except Exception as e:
            raise Exception(e)

        return res


class QuotaExceededException(Exception):
    pass

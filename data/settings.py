import os
from enum import Enum


class Settings(Enum):
    """
    設定値
    """
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
    YOUTUBE_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

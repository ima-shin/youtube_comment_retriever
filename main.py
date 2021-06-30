import pandas as pd
from googleapiclient.errors import HttpError
import os
import time
import csv
import youtube
from youtube import QuotaExceededException
from data import Streamer


class Main(object):

    def __init__(self):
        self.youtube = youtube.Youtube()
        self.video_ids = []
        self.sleep = 2
        self.quota_exceeded = False

    def save_all_videos_id_on_a_channel(self, channel_id, streamer_name):

        filename = os.path.join(os.getcwd(), f"output/{streamer_name}.csv")

        params = {"part": "snippet", "order": "date",  "channelId": channel_id}
        next_page_token = "initial"
        video_ids = []
        print(f"channel -{streamer_name}- start.")
        page_cnt = 1
        while next_page_token:
            print(f"\tpage {page_cnt}")
            res = None
            try:
                res = self.youtube.search(params=params)
            except QuotaExceededException as e:
                print(f"Quota has been exceeded while processing {streamer_name}-{page_cnt}-{channel_id}.")
                self.save_next_page_token(channel_id, next_page_token)
                self.quota_exceeded = True
                break
            except HttpError as e:
                print(e)
                self.save_next_page_token(channel_id, next_page_token)
            except Exception as e:
                print(e)
                self.save_next_page_token(channel_id, next_page_token)
                break
            if not res or not res.get("items", None):
                print("\tdone.")
                break

            for item in res.get("items"):
                if item["id"]["kind"] != "youtube#video":
                    break
                video_ids.append(item["id"]["videoId"])

            next_page_token = res.get("nextPageToken")
            params["pageToken"] = next_page_token

            page_cnt += 1
            time.sleep(self.sleep)

        print("\twriting...")
        pd.DataFrame({
            "channel_id": [channel_id] * len(video_ids),
            "video_id": pd.Series(video_ids)
        }).to_csv(filename, mode="a", encoding="utf-8", header=True, index=False)
        print("\tdone.")

        print(f"channel -{streamer_name}- completed.")

    def get_comment_threads_from_a_video(self, video_id):
        pass

    def save_next_page_token(self, channel_id, page_token):
        if not channel_id or not page_token:
            return

        filename = os.path.join(os.getcwd(), "output/resume.csv")
        if not os.path.exists(filename):
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["channel_id", "next_page_token"])

        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([channel_id, page_token])


if __name__ == "__main__":
    main = Main()
    for streamer in Streamer:
        if not main.quota_exceeded:
            main.save_all_videos_id_on_a_channel(streamer.value["channel_id"], streamer.value["name"])

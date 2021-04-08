import os
# Cron Job

from django_cron import CronJobBase, Schedule

# Google API
from googleapiclient.discovery import build
import apiclient

from .models import *
from Fampay import settings
from datetime import datetime, timedelta


class CallYoutubeApi(CronJobBase):

    RUN_EVERY_MINS = 10  # runs after every 10 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'fampayapp.call_youtube_api'    # a unique code

    def do(self):
        apiKeys = settings.GOOGLE_API_KEYS
        time_now = datetime.now()
        last_request_time = time_now - timedelta(minutes=10)

        valid = False
        for apiKey in apiKeys:
            try:
                youtube = build("youtube", "v3", developerKey=apiKey)
                req = youtube.search().list(q="music", part="snippet", order="date", maxResults=50,
                                            publishedAfter=(last_request_time.replace(microsecond=0).isoformat()+'Z'))
                res = req.execute()
                valid = True
            except apiclient.errors.HttpError as err:
                code = err.resp.status
                if not(code == 400 or code == 403):
                    break
            if valid:
                break


        if valid:
            for item in res['items']:
                video_id = item['id']['videoId']
                publishedDateTime = item['snippet']['publishedAt']
                title = item['snippet']['title']
                description = item['snippet']['description']
                thumbnailsUrls = item['snippet']['thumbnails']['default']['url']

                Videos.objects.create(
                    video_id=video_id,
                    title=title,
                    description=description,
                    publishedDateTime=publishedDateTime,
                    thumbnailsUrls=thumbnailsUrls,
                )
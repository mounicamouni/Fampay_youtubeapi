from django.db import models
#Video model
class Videos(models.Model):
    video_id = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    publishedDateTime = models.DateTimeField()
    thumbnailsUrls = models.URLField()

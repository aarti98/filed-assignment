from django.utils import timezone

from django.db import models

from rest_framework.exceptions import ValidationError


def validate_datetime(datetime):
    if datetime < timezone.now():
        raise ValidationError("Date cannot be in the past")


# model for song type of files
class SongAudioFileModel(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(validators=[validate_datetime])

    def __str__(self):
        return self.name


# model for podcast type of files
class PodcastAudioFileModel(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(validators=[validate_datetime])
    host = models.CharField(max_length=100)
    participants = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


# model for audiobook type of files
class AudiobookAudioFileModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(validators=[validate_datetime])

    def __str__(self):
        return self.title

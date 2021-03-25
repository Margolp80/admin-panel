from datetime import datetime

from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=30)
    all_day = models.BooleanField(default=False)
    start = models.DateTimeField(default=datetime.now, blank=True)
    end = models.DateTimeField(default=datetime.now, blank=True)
    desc = models.CharField(max_length=200, blank=True)
    link = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.title

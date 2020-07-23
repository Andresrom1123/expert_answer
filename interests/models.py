from django.conf import settings
from django.db import models

from topics.models import Topic


class Interest(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ManyToManyField(Topic)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

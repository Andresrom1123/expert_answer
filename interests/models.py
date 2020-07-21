from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from topics.models import Topic


class Interest(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ManyToManyField(Topic)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

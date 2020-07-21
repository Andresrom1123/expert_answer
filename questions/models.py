from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from topics.models import Topic


class Question(models.Model):
    question = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic_question')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_question')
    followers = models.ManyToManyField(User, related_name='followers_question')
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.question

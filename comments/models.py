from django.conf import settings
from django.db import models
from django.utils import timezone
from answers.models import Answer
from topics.models import Topic
from django.contrib.auth.models import User


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="topic_comment", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="answer_comment")
    created_at = models.DateTimeField(auto_created=timezone.now)

    def __str__(self):
        return self.text

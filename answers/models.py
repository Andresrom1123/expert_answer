from django.db import models
from django.utils import timezone

from expert_answer import settings
from questions.models import Question


class Answer(models.Model):
    text = models.CharField(max_length=1000)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Auser')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=timezone.now)
    vote = models.ManyToManyField(settings.AUTH_USER_MODEL, db_table="Vote_User")

    def __str__(self):
        return self.text

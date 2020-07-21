from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=150)

    def ___str__(self):
        return self.id

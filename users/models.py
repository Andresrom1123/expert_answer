from django.db import models
from django.contrib.auth.models import AbstractUser, User
from rest_framework.exceptions import ValidationError


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

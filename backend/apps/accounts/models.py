from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Email')

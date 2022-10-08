from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)

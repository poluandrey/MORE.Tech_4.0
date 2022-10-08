from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)


class Experience(models.Model):
    experience_from = models.IntegerField()
    experience_to = models.IntegerField()
    level = models.IntegerField()

    def __str__(self):
        return f'level: {str(self.level)}'

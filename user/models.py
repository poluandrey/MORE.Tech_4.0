from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    is_manager = models.BooleanField(default=False)


class Subordinates(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='managers')
    staff = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='staff')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('manager', 'staff'), name='subordinate_unique_constraind'),
        ]

    def __str__(self):
        return f'{self.manager.username}'


class Experience(models.Model):
    experience_from = models.IntegerField()
    experience_to = models.IntegerField()
    level = models.IntegerField()

    def __str__(self):
        return f'level: {str(self.level)}'

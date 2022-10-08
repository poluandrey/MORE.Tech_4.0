from django.db import models
from django.contrib.auth.models import AbstractUser

from game.models import Achievement


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


class EmployeeAchievement(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.RESTRICT, related_name='employees')

    def __str__(self):
        return f'{self.employee.username}: {self.achievement.achievement_name}'

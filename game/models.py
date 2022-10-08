from django.db import models


class Experience(models.Model):
    experience_from = models.IntegerField()
    experience_to = models.IntegerField()
    level = models.IntegerField(unique=True)

    def __str__(self):
        return f'level: {str(self.level)}'


class Achievement(models.Model):
    achievement_name = models.CharField(max_length=120)
    achievement_descr = models.TextField()

    def __str__(self):
        return self.achievement_name

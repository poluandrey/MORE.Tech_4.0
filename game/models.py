from django.db import models


class Experience(models.Model):
    experience_from = models.IntegerField()
    experience_to = models.IntegerField()
    level = models.IntegerField(unique=True)

    def __str__(self):
        return f'level: {str(self.level)}'


class Achieve(models.Model):
    achieve_name = models.CharField(max_length=120)
    achieve_descr = models.TextField()

    def __str__(self):
        return self.achieve_name

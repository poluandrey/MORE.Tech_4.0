from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import Employee
from game.models import Experience


@receiver(post_save, sender=Employee, dispatch_uid='calculate_user_level')
def calculate_employee_level(sender, instance: Employee, created=False, **kwargs):
    if not created:
        level = Experience.objects.get(experience_from__lte=instance.experience, experience_to__gt=instance.experience).level
        instance.level = level
        # instance.save()
        Employee.objects.filter(pk=instance.pk).update(level=level)

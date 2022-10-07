# Generated by Django 4.1.2 on 2022-10-07 20:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_remove_task_is_related_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='responsible',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

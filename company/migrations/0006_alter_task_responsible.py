# Generated by Django 4.1.2 on 2022-10-07 20:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0005_rename_departmentemployee_departmentstaff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='responsible',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
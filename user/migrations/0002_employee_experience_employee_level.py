# Generated by Django 4.1.2 on 2022-10-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='experience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_related',
        ),
        migrations.AddConstraint(
            model_name='departmentemployee',
            constraint=models.UniqueConstraint(fields=('department', 'employee'), name='employee_department'),
        ),
    ]

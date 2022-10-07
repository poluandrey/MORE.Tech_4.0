# Generated by Django 4.1.2 on 2022-10-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_remove_task_responsible_taskresponsible'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='departmentstaff',
            name='employee_department',
        ),
        migrations.AddConstraint(
            model_name='departmentstaff',
            constraint=models.UniqueConstraint(fields=('department', 'employee'), name='employee_department_unique'),
        ),
        migrations.AddConstraint(
            model_name='taskresponsible',
            constraint=models.UniqueConstraint(fields=('task', 'employee'), name='employee_task_unique'),
        ),
    ]

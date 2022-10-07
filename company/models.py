from django.db import models

from django_fsm import FSMField, transition

from user.models import Employee


class Department(models.Model):
    department_name = models.CharField(max_length=120)

    def __str__(self):
        return self.department_name


class DepartmentStaff(models.Model):
    department = models.ForeignKey(Department, on_delete=models.RESTRICT, related_name='departments')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employees')

    class Meta:
        constraints = [models.UniqueConstraint(fields=('department', 'employee'), name='employee_department_unique')]


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    task_status = FSMField(default='unassigned')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_tasks', null=True, blank=True)

    def __str__(self):
        return self.task_name


class TaskResponsible(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='responsible')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='tasks', null=True, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=('task', 'employee'), name='employee_task_unique')]

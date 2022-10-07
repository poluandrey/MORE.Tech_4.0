from django.contrib import admin

from company.models import Department, Task, DepartmentStaff, TaskResponsible


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'task_description', 'task_status', 'parent']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']


@admin.register(DepartmentStaff)
class DepartmentEmployeeAdmin(admin.ModelAdmin):
    list_display = ['department', 'employee']


@admin.register(TaskResponsible)
class TaskResponsibleAdmin(admin.ModelAdmin):
    list_display = ['employee', 'task']

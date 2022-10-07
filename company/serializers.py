from rest_framework import serializers

from company.models import Task, Department


class EmployeeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'task_status']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'task_description', 'task_status', 'parent']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name']

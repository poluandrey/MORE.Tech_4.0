from rest_framework import serializers

from user.models import Employee
from company.models import DepartmentStaff, TaskResponsible
from company.serializers import EmployeeTaskSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField(allow_null=True)

    def get_department(self, obj):
        try:
            department = DepartmentStaff.objects.get(employee=obj).department.department_name
        except DepartmentStaff.DoesNotExist:
            department = None
        return department

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'department', 'level', 'experience', 'is_manager']


class EmployeeTasksSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    def get_tasks(self, obj):
        try:
            tasks = [task.task for task in TaskResponsible.objects.prefetch_related().filter(employee=obj)]
        except TaskResponsible.DoesNotExist:
            tasks = None

        return EmployeeTaskSerializer(tasks, many=True).data

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'tasks', ]

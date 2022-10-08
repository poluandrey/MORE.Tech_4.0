from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from company import models
from company import serializers
from company.models import TaskResponsible
from user.models import Employee


class TaskView(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

    @action(methods=['POST'], detail=True, url_name='assigned', url_path='assigned')
    def assigned_task(self, request, *args, **kwargs):
        """assign task to user"""
        employee_id = request.data.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)
        task = self.get_object()
        TaskResponsible.objects.create(task=task, employee=employee)
        task.assign_task_to_user()
        task.save()
        return Response(status=status.HTTP_200_OK)

class DepartmentView(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

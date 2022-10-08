import django_fsm
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

    @action(methods=['POST'], detail=True, url_name='start', url_path='take-to-work')
    def take_task_to_work(self, request, *args, **kwargs):
        """take task to work"""
        task = self.get_object()
        try:
            task.get_task_in_work()
        except django_fsm.TransitionNotAllowed:
            current_status = task.task_status
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": f"can not change status from {current_status} to 'in work'"})
        task.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True, url_name='close', url_path='close')
    def close_task(self, request, *args, **kwargs):
        """close task"""
        task = self.get_object()
        try:
            task.get_task_in_work()
        except django_fsm.TransitionNotAllowed:
            current_status = task.task_status
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": f"can not change status from {current_status} to 'close'"})
        task.save()
        return Response(status=status.HTTP_200_OK)


class DepartmentView(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

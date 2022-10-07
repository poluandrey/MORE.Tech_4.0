from rest_framework import viewsets

from company import models
from company import serializers


class TaskView(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class DepartmentView(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer



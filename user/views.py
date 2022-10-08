from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import Employee, EmployeeAchievement
from user.serializers import EmployeeSerializer, EmployeeTasksSerializer
from game.serializers import AchievementSerializer
from game.models import Achievement

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(is_staff=False)
    serializer_class = EmployeeSerializer

    def get_serializer_class(self):
        if self.action == 'employee_task':
            return EmployeeTasksSerializer
        return EmployeeSerializer

    @action(methods=['GET'], detail=True, url_path='task', url_name='employee_task')
    def employee_task(self, request, *args, **kwargs):
        """return employee task"""
        employee = self.get_object()
        serializer = EmployeeTasksSerializer(employee, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True, url_path='experience', url_name='experience')
    def experience(self, request, *args, **kwargs):
        """get user experience"""
        employee = self.get_object()
        return Response(status=status.HTTP_200_OK, data={'experience': employee.experience})

    @action(methods=['POST'], detail=True, url_path='experience/increase', url_name='experience-increase')
    def increase_experience(self, request, *args, **kwargs):
        employee = self.get_object()
        exp = request.data.get('experience')
        employee.experience = employee.experience + exp
        employee.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True, url_path='achievement', url_name='achievement')
    def achievement_list(self, request, *args, **kwargs):
        employee = self.get_object()
        serializer = AchievementSerializer([achievements.achievement for achievements in employee.achievements.all()],
                                           many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True, url_path='achievement/reward', url_name='reward-achievement')
    def reward_achievement(self, request, *args, **kwargs):
        employee = self.get_object()
        achievement = get_object_or_404(Achievement, id=request.data.get('achievement_id'))
        EmployeeAchievement.objects.create(employee=employee, achievement=achievement)
        return Response(status=status.HTTP_200_OK)



from rest_framework import serializers

from game.models import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'achievement_name', 'achievement_descr']

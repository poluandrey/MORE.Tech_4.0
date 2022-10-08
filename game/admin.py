from django.contrib import admin

from game.models import Achievement, Experience


@admin.register(Achievement)
class AchieveAdmin(admin.ModelAdmin):
    list_display = ['achievement_name', 'achievement_descr']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('experience_from', 'experience_to', 'level', )
    list_editable = ['experience_from', 'experience_to', ]
    list_display_links = ['level']


from django.contrib import admin

from game.models import Achieve, Experience


@admin.register(Achieve)
class AchieveAdmin(admin.ModelAdmin):
    list_display = ['achieve_name', 'achieve_descr']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('experience_from', 'experience_to', 'level', )
    list_editable = ['experience_from', 'experience_to', ]
    list_display_links = ['level']


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Experience, Subordinates

admin.site.register(Employee, UserAdmin)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    fields = ['experience_from', 'experience_to', 'level', 'is_manager']


@admin.register(Subordinates)
class SubordinatesAdmin(admin.ModelAdmin):
    fields = ['manager', 'staff']

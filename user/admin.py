from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Subordinates, EmployeeAchievement

admin.site.register(Employee, UserAdmin)


@admin.register(Subordinates)
class SubordinatesAdmin(admin.ModelAdmin):
    list_display = ['manager', 'staff']


@admin.register(EmployeeAchievement)
class EmployeeAchievementAdmin(admin.ModelAdmin):
    list_display = ['employee', 'achievement']

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Subordinates

admin.site.register(Employee, UserAdmin)


@admin.register(Subordinates)
class SubordinatesAdmin(admin.ModelAdmin):
    list_display = ['manager', 'staff']

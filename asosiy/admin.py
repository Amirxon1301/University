from django.contrib import admin
from .models import  *

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ["name"]

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_filter = ["active"]
    search_fields = ["name"]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_filter = ["major__active", "main"]
    search_fields = ["name"]



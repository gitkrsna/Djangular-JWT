from django.contrib import admin
from .models import Students


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    ordering = ['-first_name']
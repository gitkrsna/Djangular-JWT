from django.contrib import admin
from .models import Fees, Students


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    ordering = ['-first_name']

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    ordering = ['amount']
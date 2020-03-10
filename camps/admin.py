from django.contrib import admin
from .models import * # Camp, Group, Coach, CoachList

# Register your models here.

class CoachInline(admin.TabularInline):
    model = CoachList

class GroupInLine(admin.TabularInline):
    model = Group

class CampAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'date_start', 'date_end', 'albom')
    inlines = [
            GroupInLine,
            CoachInline
            ]

admin.site.register(Coach)
admin.site.register(Camp, CampAdmin)



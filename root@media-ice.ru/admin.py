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

class ClusterItemInline(admin.TabularInline):
    model = ClusterItem

class ItemInClusterInline(admin.TabularInline):
    model = ItemInCluster

class SheduleClusterAdmin(admin.ModelAdmin):
    list_display = ('title', 'shedule', 'date_start', 'date_end')
    inlines = [ItemInClusterInline]

class SheduleClusterInline(admin.TabularInline):
    model = SheduleCluster

class ClusterItemInline(admin.ModelAdmin):
    model = ClusterItem

class SheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'camp', 'group')
    inlines = [
        SheduleClusterInline
            ]

admin.site.register(Coach)
admin.site.register(Camp, CampAdmin)


admin.site.register(Shedule, SheduleAdmin)
admin.site.register(ClusterItem)
admin.site.register(SheduleCluster, SheduleClusterAdmin)

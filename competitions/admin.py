from django.contrib import admin
from .models import Event, Participant, Category, Segment, Entry

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ('participant', 'category', 'payment' ,'music')

class EntryInLine(admin.TabularInline):
    model = Entry

class CategoryInLine(admin.TabularInline):
    model = Category

class SegmentsInline(admin.TabularInline):
    model = Segment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'date_start', 'date_end')
    inlines = [
        SegmentsInline,
        EntryInLine,
    ] 

class SegmentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'gender')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'date_start', 'date_end', 'published')
    inlines = [CategoryInLine]

admin.site.register(Event, EventAdmin)
admin.site.register(Participant)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Segment, SegmentAdmin)
admin.site.register(Entry, EntryAdmin)


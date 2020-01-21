from django.contrib import admin
from .models import Event, Participant, Category, Entry 

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ('participant', 'category')

class EntryInLine(admin.TabularInline):
    model = Entry

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'date_start', 'date_end')
    inlines = [EntryInLine] 

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)


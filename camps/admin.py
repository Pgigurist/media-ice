from django.contrib import admin
from .models import Camp

# Register your models here.

class CampAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'date_start', 'date_end',)




admin.site.register(Camp, CampAdmin)

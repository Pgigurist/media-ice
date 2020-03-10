from django.contrib import admin
from .models import * #Post, Feedback, Photo, Albom 

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    
    list_display = ('__str__', 'pub_date', 'city', 'moderate')
    list_filter = ['moderate', 'pub_date']
    search_fields = ['city']

class PhotoInline(admin.TabularInline):
    model = Photo

class AlbomAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
            ]


admin.site.register(Post)
admin.site.register(Albom, AlbomAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Photo)


from django.contrib import admin
from .models import Post, Feedback, Photo

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    
    list_display = ('pub_date', 'city', 'moderate')
    list_filter = ['moderate', 'pub_date']
    search_fields = ['city']

admin.site.register(Post)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Photo)

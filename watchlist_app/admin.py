from django.contrib import admin
from .models import WatchList,StreamPlatform
# Register your models here.
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('title','storyline')
    search_fields = ['title','storyline']
admin.site.register(WatchList, WatchListAdmin)

class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ('name','about')
    search_fields = ['name','website']
    
admin.site.register(StreamPlatform,WatchListAdmin)

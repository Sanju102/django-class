from django.contrib import admin
from .models import WatchList,StreamPlatform,Review
# Register your models here.
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('title','storyline')
    search_fields = ['title','storyline']
admin.site.register(WatchList, WatchListAdmin)

class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ('name','about')
    search_fields = ['name','website']

admin.site.register(StreamPlatform,StreamPlatformAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating','watchlist','description')
    search_fields = ['rating','watchlist']

admin.site.register(Review,ReviewAdmin)

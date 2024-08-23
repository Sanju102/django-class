from django.contrib import admin
from .models import WatchList,StreamPlatform
# Register your models here.
class WatchListAdmin(admin.ModelAdmin):
    list_display = ('title','storyline')
    search_fields = ['title','storyline']
admin.site.register(WatchList, WatchListAdmin)


# admin.site.register(StreamPlatform)

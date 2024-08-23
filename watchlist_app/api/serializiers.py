from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):

    len_of_name=serializers.SerializerMethodField() #mention the custome field


    class Meta:
        model=WatchList
        fields="__all__"

    #define the fields
    def get_len_of_name(self,object):
        return len(object.title)
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model=StreamPlatform
        fields='__all__'

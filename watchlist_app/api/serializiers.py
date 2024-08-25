from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Review
        exclude=('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    len_of_name=serializers.SerializerMethodField()


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

from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"

    #  Object-level validation   
    def validate(self, data):
        if data["name"]==data["description"]:
            raise serializers.ValidationError('Name and description cannot be same !')
        else:
            return data
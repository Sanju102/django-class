from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):

    len_of_name=serializers.SerializerMethodField() #mention the custome field


    class Meta:
        model=Movie
        fields="__all__"

    #define the fields
    def get_len_of_name(self,object):
        return len(object.name)

    #  Object-level validation   
    def validate(self, data):
        if data["name"]==data["description"]:
            raise serializers.ValidationError('Name and description cannot be same !')
        else:
            return data
from rest_framework import serializers
from watchlist_app.models import Movie

def not_less_than_two(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short !')
    else:
        return value

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(validators=[not_less_than_two])
    description=serializers.CharField()
    active=serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance

    #  Object-level validation   
    def validate(self, data):
        if data["name"]==data["description"]:
            raise serializers.ValidationError('Name and description cannot be same !')
        else:
            return data
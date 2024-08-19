from django.http import JsonResponse
from watchlist_app.models import Movie
from watchlist_app.api.serializiers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def movie_deatails(request,pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie)

    return Response(serializer.data)
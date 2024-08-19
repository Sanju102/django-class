from django.http import JsonResponse
from watchlist_app.models import Movie
from watchlist_app.api.serializiers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST'])
def movie_list(request):
    if request.method=="GET":
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data Created succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)

@api_view(['GET'])
def movie_deatails(request,pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie)

    return Response(serializer.data)
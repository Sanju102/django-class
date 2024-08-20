from django.http import JsonResponse
from watchlist_app.models import Movie
from watchlist_app.api.serializiers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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

@api_view(['GET','PUT','DELETE'])
def movie_deatails(request,pk):
    if request.method=="GET":
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'message':'Movie not found !'}, status=status.HTTP_404_NOT_FOUND)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Message':'Movie matching query does not exist'},status=status.HTTP_400_BAD_REQUEST)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data updated succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)
    elif request.method=="DELETE":
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response({'message':"data deleted succesfully !"})
    
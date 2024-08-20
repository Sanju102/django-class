from django.http import JsonResponse
from watchlist_app.models import Movie
from watchlist_app.api.serializiers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MovieList(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        
        return Response(serializer.data)
    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data Created succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)

class MovieDetails(APIView):
    def get(self,request,pk):
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'message':'Movie not found !'}, status=status.HTTP_404_NOT_FOUND)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
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
    
    def delete(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response({'message':"data deleted succesfully !"})

from django.http import JsonResponse
from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializiers import WatchListSerializer,StreamPlatformSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WatchListList(APIView):
    def get(self,request):
        WatchLists=WatchList.objects.all()
        serializer=WatchListSerializer(WatchLists,many=True)
        
        return Response(serializer.data)
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data Created succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)

class WatchListDetails(APIView):
    def get(self,request,pk):
        try:
            WatchList=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'message':'WatchList not found !'}, status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(WatchList)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            WatchList=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Message':'WatchList matching query does not exist'},status=status.HTTP_400_BAD_REQUEST)
        serializer=WatchListSerializer(WatchList,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data updated succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        WatchList=WatchList.objects.get(pk=pk)
        WatchList.delete()
        return Response({'message':"data deleted succesfully !"})
    

class StreamPlatformList(APIView):
    def get(self,request):
        StreamPlatforms=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(StreamPlatforms,many=True)
        
        return Response(serializer.data)
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data Created succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetails(APIView):
    def get(self,request,pk):
        try:
            StreamPlatform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'message':'StreamPlatform not found !'}, status=status.HTTP_404_NOT_FOUND)
        serializer=StreamPlatformSerializer(StreamPlatform)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            StreamPlatform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Message':'StreamPlatform matching query does not exist'},status=status.HTTP_400_BAD_REQUEST)
        serializer=StreamPlatformSerializer(StreamPlatform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data updated succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        StreamPlatform=StreamPlatform.objects.get(pk=pk)
        StreamPlatform.delete()
        return Response({'message':"data deleted succesfully !"})


from django.http import JsonResponse
from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializiers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSerializer
    def perform_create(self, serializer):
        serializer.save(watchlist=WatchList.objects.get(pk=self.kwargs['pk']))

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        # print(self.request)
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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
            watch_list=WatchList.objects.get(pk=pk)
        except watch_list.DoesNotExist:
            return Response({'message':'WatchList not found !'}, status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(watch_list)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            watch_list=WatchList.objects.get(pk=pk)
        except watch_list.DoesNotExist:
            return Response({'Message':'WatchList matching query does not exist'},status=status.HTTP_400_BAD_REQUEST)
        serializer=WatchListSerializer(watch_list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data updated succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        watch_list=WatchList.objects.get(pk=pk)
        watch_list.delete()
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
            stream_platform=StreamPlatform.objects.get(pk=pk)
        except stream_platform.DoesNotExist:
            return Response({'message':'StreamPlatform not found !'}, status=status.HTTP_404_NOT_FOUND)
        serializer=StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            stream_platform=StreamPlatform.objects.get(pk=pk)
        except stream_platform.DoesNotExist:
            return Response({'Message':'StreamPlatform matching query does not exist'},status=status.HTTP_400_BAD_REQUEST)
        serializer=StreamPlatformSerializer(stream_platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data updated succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        stream_platform=StreamPlatform.objects.get(pk=pk)
        stream_platform.delete()
        return Response({'message':"data deleted succesfully !"})


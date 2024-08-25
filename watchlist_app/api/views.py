from watchlist_app.api.permissions import AdminorReadonly, ReviewUserorReadonly
from django.http import JsonResponse
from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializiers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSerializer
    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self, serializer):
        watchlist=WatchList.objects.get(pk=self.kwargs['pk'])
        queryset = Review.objects.filter(review_user=self.request.user,watchlist=watchlist)
        if queryset.exists():
            raise ValidationError('You have already gave a review')
        serializer.save(review_user=self.request.user,watchlist=watchlist)
        # watchlist=WatchList.objects.get(pk=self.kwargs['pk'])
        # user=self.request.user
        # reviewqueryset=Review.objects.filter(watchlist=watchlist,review_user=user)
        # if reviewqueryset.exists():
        #     raise ValidationError("user already gave review for  this content")
        # serializer.save()

class ReviewList(generics.ListAPIView):
    permission_classes=[AdminorReadonly]
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        # print(self.request)
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[ReviewUserorReadonly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class WatchListViewSet(viewsets.ModelViewSet):
    permission_classes=[AdminorReadonly]
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

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
    permission_classes=[AdminorReadonly]
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
    
class StreamPlatformViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        platform = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def create(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'message':'Data Created succesfully !!'}
            return Response(data)
        else:
            return Response(serializer.errors)
        
    def update(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        platform = get_object_or_404(queryset, pk=pk)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

from django.urls import path
from .views import WatchListList,WatchListDetails,StreamPlatformDetails,StreamPlatformList

urlpatterns = [
    path('watchlist/list/', WatchListList.as_view(), name='WatchList-list' ),
    path('streamplatform/list/', StreamPlatformList.as_view(), name='StreamPlatform-list' ),
    path('watchlist/<int:pk>', WatchListDetails.as_view(), name='WatchList-details'),
    path('streamplatform/<int:pk>', StreamPlatformDetails.as_view(), name='StreamPlatform-details'),
]
from django.urls import path
from .views import ReviewDetail,ReviewCreate,ReviewList, WatchListList,WatchListDetails,StreamPlatformDetails,StreamPlatformList

urlpatterns = [
    path('watchlist/list/', WatchListList.as_view(), name='WatchList-list' ),
    path('streamplatform/list/', StreamPlatformList.as_view(), name='StreamPlatform-list' ),
    path('watchlist/<int:pk>', WatchListDetails.as_view(), name='WatchList-details'),
    path('streamplatform/<int:pk>', StreamPlatformDetails.as_view(), name='StreamPlatform-details'),
    path('watchlist/<int:pk>/reviews/', ReviewList.as_view(), name='Review-list' ),
    path('watchlist/<int:pk>/review-create/', ReviewCreate.as_view(), name='Review-craete' ),
    path('review/<int:pk>', ReviewDetail.as_view(), name='Review-details'),
]
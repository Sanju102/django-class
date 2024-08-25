from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (StreamPlatformViewSet, ReviewDetail,ReviewCreate,ReviewList,
                     WatchListList,WatchListDetails)

router = DefaultRouter()
router.register('streamplatform',StreamPlatformViewSet,basename="streamplatform")
urlpatterns = [
    path('',include(router.urls)),
    path('watchlist/list/', WatchListList.as_view(), name='WatchList-list' ),
    path('watchlist/<int:pk>', WatchListDetails.as_view(), name='WatchList-details'),
    path('watchlist/<int:pk>/reviews/', ReviewList.as_view(), name='Review-list' ),
    path('watchlist/<int:pk>/review-create/', ReviewCreate.as_view(), name='Review-craete' ),
    path('review/<int:pk>', ReviewDetail.as_view(), name='Review-details'),
]
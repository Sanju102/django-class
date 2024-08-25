from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (StreamPlatformViewSet, ReviewDetail,ReviewCreate,ReviewList,
                     WatchListList,WatchListDetails,WatchListViewSet)

router = DefaultRouter()
router.register('streamplatform',StreamPlatformViewSet,basename="streamplatform")
router.register('watchlist',WatchListViewSet,basename="watchlist")
urlpatterns = [
    path('',include(router.urls)),
    path('watchlist/<int:pk>/reviews/', ReviewList.as_view(), name='Review-list' ),
    path('watchlist/<int:pk>/review-create/', ReviewCreate.as_view(), name='Review-craete' ),
    path('review/<int:pk>', ReviewDetail.as_view(), name='Review-details'),
]
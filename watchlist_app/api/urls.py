from django.urls import path
from .views import movie_list,movie_deatails

urlpatterns = [
    path('list/', movie_list, name='movie-list' ),
    path('<int:pk>', movie_deatails, name='movie-details'),
]
from django.urls import path,include
from rest_framework.authtoken.views import ObtainAuthToken
from .views import register_user,logout_user

urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name='login-token' ),
    path('logout/', logout_user, name='logout-token' ),
    path('register/', register_user, name='register' ),
]
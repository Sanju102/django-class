from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['POST'])
def register_user(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Hello, world!"})
@api_view(['POST'])
def logout_user(request):
    if request.method=='POST':
        username=request.user.username
        user=User.objects.get(username=username) 
        # password=request.POST.get(password)
        token=Token.objects.filter(user=user)
        token.delete()
        return Response({"message":"Log out succesfully"})
        

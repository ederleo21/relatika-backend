from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer

class RegisterUserCreateAPIView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]


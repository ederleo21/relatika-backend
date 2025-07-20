from rest_framework import generics
from apps.users.models import CustomUser
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer

class RegisterUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]
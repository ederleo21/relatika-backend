from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import CustomUser

from .serializers import UserSerializer

class UserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class UserDetailView(RetrieveAPIView):
    queryset = UserSerializer.Meta.model.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class pruebas(APIView):

    def get(self, request):
        user = CustomUser.objects.get(pk=25)
        siguiendo = user.followers.all()
        print(siguiendo)
        return Response({""})
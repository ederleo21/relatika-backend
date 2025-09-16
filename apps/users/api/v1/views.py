from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import CustomUser, Follow

from .serializers import UserSerializer, UserProfileSerializer

class UserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class UserDetailView(RetrieveAPIView):
    queryset = UserSerializer.Meta.model.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class FollowUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            userAuthId = self.request.user.id
            userId = request.data["userId"]

            if not CustomUser.objects.filter(id=userId).exists():
                return Response({"error": "Usuario no existe"}, status=status.HTTP_404_NOT_FOUND)
            
            Follow.objects.create(follower_id=userAuthId, following_id=userId)
            return Response(status=status.HTTP_201_CREATED)
        
        except Exception:
            return Response({"error": "Ya sigues a este usuario"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        userAuthId = self.request.user.id
        userId = request.query_params.get("userId")

        if not userId:
            return Response({"error": "Falta el id del usuario"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Follow.objects.get(follower_id=userAuthId, following_id=userId).delete()
            return Response(status=status.HTTP_200_OK)
        except Follow.DoesNotExist:
            return Response({"error": "Tú no sigues a este usuario"}, status=status.HTTP_404_NOT_FOUND)


class pruebas(APIView):

    def get(self, request):
        user = CustomUser.objects.get(pk=25)
        siguiendo = user.followers.all()
        print(siguiendo)
        return Response({""})
    
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import RegisterUserSerializer

class UserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
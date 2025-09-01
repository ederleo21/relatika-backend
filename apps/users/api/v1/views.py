from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

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
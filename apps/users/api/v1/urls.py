from django.urls import path
from .auth import CustomTokenObtainPairView, CustomTokenRefreshView, RegisterUserListCreateView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('users/', RegisterUserListCreateView.as_view(), name="users")
]
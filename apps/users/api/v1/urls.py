from django.urls import path
from .auth import CustomTokenObtainPairView, CustomTokenRefreshView, RegisterUserCreateView

urlpatterns = [
    path('register/', RegisterUserCreateView.as_view(), name="register_user"),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
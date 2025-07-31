from django.urls import path
from .auth import CustomTokenObtainPairView, CustomTokenRefreshView, RegisterUserCreateView
from .users import UserProfileView

urlpatterns = [
    path('register/', RegisterUserCreateView.as_view(), name="register_user"),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    path('profile/', UserProfileView.as_view(), name="user_profile")
]
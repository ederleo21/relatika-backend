from django.urls import path
from .auth import CustomTokenObtainPairView, CustomTokenRefreshView, RegisterUserCreateView, LogoutView
from .users import UserProfileView

urlpatterns = [
    path('register/', RegisterUserCreateView.as_view(), name="register_user"),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name="logout"),

    path('profile/', UserProfileView.as_view(), name="user_profile")
]
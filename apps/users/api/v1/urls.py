from django.urls import path
from .views import UserProfileView, UserDetailView, FollowUserAPIView, FollowerList, FollowingList

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name="user_profile"),
    path('user/<int:pk>/', UserDetailView.as_view(), name="user_detail"),
    path('follow/', FollowUserAPIView.as_view(), name="follow_user"),
    path('followers/<int:pk>/', FollowerList.as_view(), name="follewer_list"),
    path('following/<int:pk>/', FollowingList.as_view(), name="following_list"),
]
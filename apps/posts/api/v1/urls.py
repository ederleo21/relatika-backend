from django.urls import path, include
from .views import PostCreateListView, PostDetailView

urlpatterns = [
    path("posts/", PostCreateListView.as_view(), name="posts"), #general feed
    path("posts/<int:pk>/", PostCreateListView.as_view(), name="posts"), #user feed
    path("post/<int:pk>/", PostDetailView.as_view(), name="posts_detail") #detail post
]
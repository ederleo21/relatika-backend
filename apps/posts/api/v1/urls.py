from django.urls import path, include
from .views import PostCreateListView

urlpatterns = [
    path("posts/", PostCreateListView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostCreateListView.as_view(), name="posts"),
]
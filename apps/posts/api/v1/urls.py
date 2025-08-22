from django.urls import path, include
from .views import PostCreateListView

urlpatterns = [
    path("posts/", PostCreateListView.as_view(), name="posts")
]
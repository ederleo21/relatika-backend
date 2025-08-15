from django.urls import path, include
from .views import PostCreateListView

urlpatterns = [
    path("post/", PostCreateListView.as_view(), name="post")
]
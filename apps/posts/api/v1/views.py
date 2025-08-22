from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from apps.posts.models import Post, PostImage
from .serializers import PostSerializer, PostImageSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db import transaction

class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                post_serializer = self.get_serializer(data=request.data)
                post_serializer.is_valid(raise_exception=True)
                post = post_serializer.save(user=request.user)

                images_list = request.FILES.getlist('images')
                for img in images_list:
                    PostImage.objects.create(post=post, image=img)

                return Response(post_serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({ "error": str(e) }, status.HTTP_400_BAD_REQUEST) 
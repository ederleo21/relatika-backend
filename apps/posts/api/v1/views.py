from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from utils.pagination import TwentyResultsSetPagination
from apps.posts.models import Post, PostImage
from .serializers import PostSerializer

class PostCreateListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    pagination_class = TwentyResultsSetPagination

    def get_queryset(self):
        user_pk = self.kwargs.get('pk')
        if user_pk:
            return Post.objects.filter(user__id=user_pk)
        return Post.objects.all()

    def create(self, request, *args, **kwargs):
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
from rest_framework import serializers
from apps.posts.models import Post, PostImage

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content']


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['post', 'image']
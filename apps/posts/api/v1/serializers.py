from rest_framework import serializers
from apps.posts.models import Post, PostImage

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['post', 'image']

    def to_representation(self, instance):
        return {
            "image": instance.image.url if instance.image else None
        }

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['user', 'title', 'content', 'images']
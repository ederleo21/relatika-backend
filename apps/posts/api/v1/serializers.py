from rest_framework import serializers
from apps.posts.models import Post, PostImage

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage

    def to_representation(self, instance):
        return {
            "image": instance.image.url if instance.image else None
        }

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'images']
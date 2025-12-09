from rest_framework import serializers
from apps.posts.models import Post, PostImage
from apps.users.api.v1.serializers import UserMiniSerializer

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage

    def to_representation(self, instance):
        request = self.context.get('request')
        url = instance.image.url if instance.image else None
        
        if request and url:
            url = request.build_absolute_uri(url)

        return {"image": url}

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    images = PostImageSerializer(many=True, read_only=True)
    user = UserMiniSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'images', 'created_at'] 
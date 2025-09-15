from rest_framework import serializers
from apps.users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    following = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'birth_date', 'avatar', 'following']
    
    def get_following(self, obj):
        return list(obj.following.values_list('following_id', flat=True))
from rest_framework import serializers
from apps.users.models import CustomUser

class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', "last_name", 'username', 'avatar']


#Serializers base con campos para perfil y usuarios normales. 
class UserBaseSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    featured_friends = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField() 
    following_count = serializers.SerializerMethodField() 

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name','bio', 'birth_date', 'avatar', 'featured_friends', 'followers_count', 'following_count']

    def get_featured_friends(self, obj):
        last_follows = obj.following.order_by('-created_at')[:5]
        friends = [follow.following for follow in last_follows] 
        return UserMiniSerializer(friends, many=True, context=self.context).data

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count() 


#Serializers personalizado para perfil de usuario (Update, delete, detail)
class UserProfileSerializer(UserBaseSerializer):
    following = serializers.SerializerMethodField()

    class Meta(UserBaseSerializer.Meta):
        fields = UserBaseSerializer.Meta.fields + ['following']
    
    def get_following(self, obj):
        return list(obj.following.values_list('following_id', flat=True))
    

#Serializer con imformacion de cualquier usuario (Solo ver)
class UserSerializer(UserBaseSerializer):

    class Meta(UserBaseSerializer.Meta):
        model = CustomUser
        fields = UserBaseSerializer.Meta.fields 

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserFollowing

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_pic', 'bio', 'website', 'followers', 'following')
        extra_kwargs = {
            'password': { 'write_only': True },
        }
    
    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data
    
    def get_followers(self, obj):
        return FollowingSerializer(obj.followers.all(), many=True).data

class FollowingSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = UserFollowing
        fields = ("id", "user", "following_user", "followed_at")
        extra_kwargs = {
            'user': { 'read_only': True },
            'following_user': { 'read_only': True }
        }
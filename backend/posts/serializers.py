from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_pic', 'bio', 'website')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['owner']
        extra_kwargs = {
            'likes': { 'read_only': True },
            'created_at': { 'read_only': True }
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)

        owner = UserSerializer(data=instance.owner.__dict__)
        owner.is_valid()
        response["owner"] = owner.data        
        
        return response

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('post', 'owner')
        extra_kwargs = {
            'likes': { 'read_only': True },
            'created_at': { 'read_only': True }
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        
        owner = UserSerializer(data=instance.owner.__dict__)
        owner.is_valid()
        response["owner"] = owner.data
        
        return response
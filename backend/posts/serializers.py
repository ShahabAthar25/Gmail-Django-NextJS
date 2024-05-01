from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer:
    class Meta:
        model = User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    likes = UserSerializer(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = "__all__"
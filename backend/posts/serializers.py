from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.RelatedField(source="user", read_only=True)
    author_handler = serializers.CharField(read_only=True, default=User.username)
    display_name = serializers.CharField(read_only=True, default=f"{User.first_name} {User.last_name}")
    created_at = serializers.DateTimeField(read_only=True)
    likes = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = "__all__"
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        
        new_response = { "msg": { "post": response } }
        return new_response
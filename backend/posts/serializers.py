from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_pic', 'bio', 'website')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('owner', 'created_at', 'likes')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        
        owner = UserSerializer(data=instance.owner.__dict__)
        owner.is_valid()
        response["owner"] = owner.data
        
        new_response = { "msg": { "post": response } }
        return new_response
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post

class ListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class RetrieveUpdateDestroyPostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]
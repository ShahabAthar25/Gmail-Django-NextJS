from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .permissions import IsOwner

class ListCreatePostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RetrieveUpdateDestroyPostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self, request, pk):
        user = request.user
        msg = ""

        post = get_object_or_404(Post, pk=pk)

        if len(post.likes.filter(id=user.id)) < 1:
            post.likes.add(user)
            msg = f"Post (with the id of {post.pk}) has been liked"
        else:
            post.likes.remove(user)
            msg = f"Removed like from Post (with the id of {post.pk})"

        post.save()
        
        return Response({ "msg": msg })

class ListCreateCommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        id = self.kwargs.get('pk')
        print(Comment.objects.filter(post=id))
        return Comment.objects.filter(post=id)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        serializer.save(owner=self.request.user, post=post)
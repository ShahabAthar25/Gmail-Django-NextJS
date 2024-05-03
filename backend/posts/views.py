from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .permissions import IsOwnerPermission
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

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
    permission_classes = [IsOwnerPermission]

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
        return Comment.objects.filter(post=id)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        serializer.save(owner=self.request.user, post=post)

class UpdateDestroyCommentView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerPermission]
    lookup_field = "pk"

    def put(self, request, *args, **kwargs):
        return self.update(request=request)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request=request)

class LikeCommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self, request, pk):
        user = request.user
        msg = ""

        comment = get_object_or_404(Comment, pk=pk)

        if len(comment.likes.filter(id=user.id)) < 1:
            comment.likes.add(user)
            msg = f"Comment (with the id of {comment.pk}) has been liked"
        else:
            comment.likes.remove(user)
            msg = f"Removed like from comment (with the id of {comment.pk})"

        comment.save()
        
        return Response({ "msg": msg })
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwner
from .serializers import PostSerializer
from .models import Post

class ListCreateView(generics.ListCreateAPIView):
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

        post = Post.objects.get(id=pk)

        if len(post.likes.filter(id=user.id)) < 1:
            post.likes.add(user)
            msg = f"Post (with the id of {post.pk}) has been liked"
        else:
            post.likes.remove(user)
            msg = f"Removed like from Post (with the id of {post.pk})"

        post.save()
        
        return Response({ "msg": msg })
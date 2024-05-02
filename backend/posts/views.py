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
    def post(self, request, pk):
        post = Post.objects.filter(pk=pk)
        print(post.likes.filter(pk=request.user.id))
        post.likes.add(request.user)
        post.save()
        
        return Response({ "msg": f"Post (with the id of {post.pk}) has been liked" })
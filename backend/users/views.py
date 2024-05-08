from rest_framework import permissions, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, FollowingSerializer
from .permissions import IsOwnerOrReadOnlyPermission
from .models import UserFollowing
from .exceptions import AlreadyFollowsUserException

User = get_user_model()

class WhoAmIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnlyPermission, permissions.IsAuthenticated]
    lookup_field = "pk"

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class SearchUsersView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        search_query = self.request.GET.get('q', None)
        if not search_query:
            raise ValidationError(detail="Url parameter 'q' was not provided.")
        return User.objects.filter(username__contains=search_query)

class FollowUnfollowUser(generics.CreateAPIView):
    queryset = UserFollowing.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowingSerializer
    
    def perform_create(self, serializer):
        try:
            following_user = User.objects.get(id=self.kwargs.get('pk'))
        except:
            raise NotFound(detail='User not found.')

        try:
            serializer.save(user=self.request.user, following_user=following_user)
        except IntegrityError:
            raise AlreadyFollowsUserException()
    
    def delete(self, request, pk):
        following_user = get_object_or_404(User, pk=pk)
        try:
            user_following = UserFollowing.objects.get(user=request.user, following_user=following_user)
        except UserFollowing.DoesNotExist:
            return Response({ "details": "You have not followed this user" }, status=404)

        user_following.delete()
        
        return Response(status=204)
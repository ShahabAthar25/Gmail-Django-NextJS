from rest_framework import permissions, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, FollowingSerializer
from .permissions import IsOwnerOrReadOnlyPermission
from .models import UserFollowing

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
        print(self.request.user.id)
        try:
            following_user = User.objects.get(id=self.kwargs.get('pk'))
        except:
            raise NotFound(detail='User not found.')

        serializer.save(user=self.request.user, following_user=following_user)
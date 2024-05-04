from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnlyPermission

User = get_user_model()

class WhoAmIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(pk=request.user.pk)
        user_data = UserSerializer(data=user.__dict__)
        user_data.is_valid()

        return Response(user_data.data)


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
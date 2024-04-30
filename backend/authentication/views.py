from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, WhoAmISerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        
        return Response({ "msg": { "user": serializer.data, "access_token": str(refresh.access_token), 'refresh_token': str(refresh) } })

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if not user:
            return Response({ "details": "Invalid Credentails" }, status=400)
        
        user_data = UserSerializer(data=user.__dict__)
        user_data.is_valid()
        
        refresh = RefreshToken.for_user(user)
        
        return Response({ "msg": { "user": user_data.data, "access_token": str(refresh.access_token), 'refresh_token': str(refresh) } })
    
class WhoAmIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = User.objects.get(pk=request.user.pk)
        user_data = UserSerializer(data=user.__dict__)
        user_data.is_valid()
        
        return Response({ "msg": { "user": user_data.data } })
from django.urls import path
from .views import RegisterView, LoginView, WhoAmIView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('whoami/', WhoAmIView.as_view(), name='whoami'),
]

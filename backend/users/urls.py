from django.urls import path
from .views import WhoAmIView, RetrieveUpdateDestroyUser

urlpatterns = [
    path('whoami/', WhoAmIView.as_view(), name='whoami'),
    path('<int:pk>/', RetrieveUpdateDestroyUser.as_view(), name='retrieve-update-destroy-user'),
]

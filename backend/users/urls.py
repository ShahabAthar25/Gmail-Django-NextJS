from django.urls import path
from .views import WhoAmIView, RetrieveUpdateDestroyUser, SearchUsersView

urlpatterns = [
    path('whoami/', WhoAmIView.as_view(), name='whoami'),
    path('<int:pk>/', RetrieveUpdateDestroyUser.as_view(), name='retrieve-update-destroy-user'),
    
    path('search/', SearchUsersView.as_view(), name=""),
]

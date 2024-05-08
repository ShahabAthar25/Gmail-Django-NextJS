from django.urls import path
from .views import WhoAmIView, RetrieveUpdateDestroyUser, SearchUsersView, FollowUnfollowUser

urlpatterns = [
    path('whoami/', WhoAmIView.as_view(), name='whoami'),
    path('search/', SearchUsersView.as_view(), name="search-user"),
    path('<int:pk>/', RetrieveUpdateDestroyUser.as_view(), name='retrieve-update-destroy-user'),
    path('<int:pk>/follow/', FollowUnfollowUser.as_view(), name="follow-unfollow-user"),
]

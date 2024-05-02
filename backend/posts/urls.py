from django.urls import path
from .views import ListCreateView, RetrieveUpdateDestroyPostView, LikePostView

urlpatterns = [
    path('', ListCreateView.as_view(), name="list-create-post"),
    path('<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), name="retrieve-update-destroy-post"),
    path('<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), name="retrieve-update-destroy-post"),
    path('<int:pk>/like', LikePostView.as_view(), name="like-post"),
]

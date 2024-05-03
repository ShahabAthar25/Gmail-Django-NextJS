from django.urls import path
from .views import ListCreatePostView, RetrieveUpdateDestroyPostView, LikePostView, ListCreateCommentView

urlpatterns = [
    path('', ListCreatePostView.as_view(), name="list-create-post"),
    path('<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), name="retrieve-update-destroy-post"),
    path('<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), name="retrieve-update-destroy-post"),
    path('<int:pk>/like', LikePostView.as_view(), name="like-post"),

    path('<int:pk>/comment/', ListCreateCommentView.as_view(), name="like-post"),
]

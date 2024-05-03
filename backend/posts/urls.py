from django.urls import path
from .views import ListCreatePostView, RetrieveUpdateDestroyPostView, LikePostView, ListCreateCommentView, UpdateDestroyCommentView, LikeCommentView

urlpatterns = [
    path('', ListCreatePostView.as_view(), name="list-create-post"),
    path('<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), name="retrieve-update-destroy-post"),
    path('<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), name="retrieve-update-destroy-post"),
    path('<int:pk>/like/', LikePostView.as_view(), name="like-post"),

    path('<int:post_id>/comment/<int:pk>/', UpdateDestroyCommentView.as_view(), name="update-destroy-comment"),
    path('<int:pk>/comment/', ListCreateCommentView.as_view(), name="list-create-comment"),
    path('comment/<int:pk>/like/', LikeCommentView.as_view(), name="update-destroy-comment"),
]

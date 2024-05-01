from django.urls import path
from .views import ListCreateView, RetrieveUpdateDestroyPostView

urlpatterns = [
    path('', ListCreateView.as_view(), name="list-create-post"),
    path('<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), name="retrieve-update-destroy-post"),
]

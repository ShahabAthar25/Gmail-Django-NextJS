from django.urls import path
from .views import getRoute

urlpatterns = [
    path('register/', getRoute, name="register"),
]

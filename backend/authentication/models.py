from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
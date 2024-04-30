from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_pic = models.ImageField(blank=True, null=True)
    website = models.CharField(max_length=200, validators=[MinLengthValidator(10)], blank=True, null=True)
    bio = models.CharField(max_length=150, validators=[MinLengthValidator(1)], blank=True, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to="users/", blank=True, null=True)
    website = models.CharField(max_length=200, validators=[MinLengthValidator(10)], blank=True, null=True)
    bio = models.CharField(max_length=150, validators=[MinLengthValidator(1)], blank=True, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    def count_followers(self):
        return self.followers.count()

class UserFollowing(models.Model):
    user = models.ForeignKey("User", related_name="following", on_delete=models.CASCADE)
    following_user = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'following_user')
        ordering = ["-followed_at"]
        
    def __str__(self):
        return f"{self.user} follows {self.following_user}"
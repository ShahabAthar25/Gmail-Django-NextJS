from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="posts")

    def __str__(self):
        return f"{self.content} | {self.author}"
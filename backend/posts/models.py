from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=2200, blank=True, null=True)
    image = models.ImageField(upload_to="posts/")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="posts", blank=True)

    def __str__(self):
        return f"{self.content} | {self.owner}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=2200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="comments", blank=True)
    
    def __str__(self):
        return f"{self.owner} | {self.post.content}"
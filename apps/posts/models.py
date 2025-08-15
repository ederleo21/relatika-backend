from django.db import models
from apps.users.models import CustomUser

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts', verbose_name="Author user")
    title = models.CharField(max_length=250, verbose_name="Title", blank=True, null=True)
    content = models.TextField(verbose_name="post content")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post by {self.user} - {self.created_at.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-created_at']


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images', verbose_name="Post")
    image = models.ImageField(upload_to="posts/images/", verbose_name="Post image")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for post id:{self.post.id} by {self.post.user}"

    class Meta: 
        ordering = ['-uploaded_at']
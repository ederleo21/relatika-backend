from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True, verbose_name="Bibliography")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Birthdate")
    avatar = models.ImageField(upload_to='users/avatars/', default="users/avatars/avatar_default.png", blank=True, null=True, verbose_name="Avatar")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['-date_joined']


class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")
        indexes = [
            models.Index(fields=["follower"]),
            models.Index(fields=["following"])
        ]

    def __str__(self):
        return f"{self.follower.username} -> {self.following.username}"

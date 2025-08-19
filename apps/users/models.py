from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True, verbose_name="Bibliography")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Birthdate")
    avatar = models.ImageField(upload_to='users/avatars/', default="users/avatars/avatar_default.png", blank=True, null=True, verbose_name="Avatar")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['-date_joined']
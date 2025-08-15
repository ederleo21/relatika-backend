from django.contrib import admin
from .models import Post, PostImage

admin.site.register([Post, PostImage])
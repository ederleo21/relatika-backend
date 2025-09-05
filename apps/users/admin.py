from django.contrib import admin
from .models import CustomUser, Follow

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_active', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Follow)
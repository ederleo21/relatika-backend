from django.urls import path
from .views import UserProfileView, UserDetailView, pruebas

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name="user_profile"),
    path('user/<int:pk>/', UserDetailView.as_view(), name="user_detail"),
    path("prueba/", pruebas.as_view(), name="prueba")
]
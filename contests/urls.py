from django.urls import path
from . import views

urlpatterns = [
    path('api/muz/', views.ImageListCreate.as_view()),
    path('api/rotate_image/', views.RotateImage.as_view())
]
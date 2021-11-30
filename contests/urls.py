from django.urls import path
from . import views

urlpatterns = [
    path('api/muz/', views.ImageListCreate.as_view()),
]
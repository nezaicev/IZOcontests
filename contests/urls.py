from django.urls import path
from . import views

urlpatterns = [
    path('api/muz/', views.ImageListCreate.as_view()),
    path('api/rotate_image_artakiada/', views.RotateModelImageArtakiada.as_view()),
    path('api/rotate_image_nrusheva/', views.RotateModelImageNRusheva.as_view())
]
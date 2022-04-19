from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vp/', views.index),
    path('artakiada/', views.index),
    path('api/archive/', views.ArchiveAPIView.as_view({'get': 'list'})),
    path('api/archive/nominationvp/', views.NominationVPAPIView.as_view()),
    path('api/archive/theme/artakiada/', views.ThemeArtakiadaAPIView.as_view()),
    path('api/archive/theme/nrusheva/', views.ThemeNRushevaAPIView.as_view())
]

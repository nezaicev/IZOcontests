from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/archive/', views.ArchiveAPIView.as_view({'get': 'list'})),
    path('api/archive/nominationvp', views.DirectionVP_API_View.as_view())
]

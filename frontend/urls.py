from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vp/', views.index),
    path('api/archive/', views.ArchiveAPIView.as_view({'get': 'list'})),
    path('api/archive/nominationvp', views.NominationVP_API_View.as_view())
]

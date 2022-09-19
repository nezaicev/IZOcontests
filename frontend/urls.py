from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vp/', views.index),
    path('artakiada/', views.index),
    path('nrusheva/', views.index),
    path('mymoskvichi/', views.index),
    path('event/', views.index),
    path('api/archive/', views.ArchiveAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('api/archive/nominationvp/', views.NominationVPAPIView.as_view()),
    path('api/archive/nomination/mymoskvichi',
         views.NominationMymoskvichiAPIView.as_view()),
    path('api/archive/theme/artakiada/',
         views.ThemeArtakiadaAPIView.as_view()),
    path('api/archive/theme/nrusheva/', views.ThemeNRushevaAPIView.as_view()),
    path('api/archive/contest/nominations/',
         views.NominationContestAPIView.as_view()),
    path('api/archive/contest/thems/', views.ThemeContestAPIView.as_view()),
    path('api/archive/contest/years/', views.YearContestAPIView.as_view()),
    path('api/contest/creative_tack/', views.CreativeTackAPIView.as_view()),
]

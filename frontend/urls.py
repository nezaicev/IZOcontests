from django.urls import path, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [

    path('', views.index),
    path('vp/', views.index),
    path('artakiada/', views.index),
    path('nrusheva/', views.index),
    path('mymoskvichi/', views.index),
    path('event/', views.index),
    path('broadcast/', views.index),
    path('broadcasts/', views.index),

    path('api/auth/',views.AuthView.as_view()),
    path('api/archive/',
         views.ArchiveAPIView.as_view({'get': 'list', 'post': 'create'})),
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
    path('api/events/', views.EventListView.as_view()),
    path('api/event/<int:pk>/', views.EventDetailView.as_view()),
    path('api/broadcasts/', views.BroadcastListView.as_view()),
    path('api/broadcast/<int:pk>/', views.BroadcastDetailView.as_view()),
    path('api/participant_event/', csrf_exempt(views.ParticipantEventDetailView.as_view())),
    path('api/participant_event_list/', views.ParticipantEventListView.as_view()),

    re_path(r'.*', views.index),

]



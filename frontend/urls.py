from django.urls import path, re_path

from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [

    path('api/auth/',views.AuthView.as_view()),
    path('api/archive/',views.ArchiveAPIView.as_view({'get': 'list', 'post': 'create'})),

    path('api/archive/art_challenge/',views.ArtChallengeAPIView.as_view({'get': 'list', 'post': 'create'})),

    path('api/archive/design/', views.DesignArchiveView.as_view({'get': 'list'})),
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
    path('api/exposition_list', views.ExpositionListAPIView.as_view()),
    path('api/expositions_years/', views.YearExpositionsArchiveAPIView.as_view()),
    path('api/exposition/<int:pk>/', views.ExpositionDetailAPIView.as_view()),
    path('api/page/<slug:slug>/', views.PageDetailAPIView.as_view()),
    path('api/contests/', views.PageContestAPIView.as_view()),
    path('api/statistics/', views.StatAPIView.as_view()),
    path('api/video/', views.VideoAPIView.as_view()),
    path('api/video/categories/', views.CategoryAPIView.as_view()),
    path('api/publication/', views.PublicationAPIView.as_view()),
    path('api/publication_years/', views.PublicationYearsAPIView.as_view())



]



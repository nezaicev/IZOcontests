from django.urls import path
from event.views import StatView

urlpatterns = [
    path('stat/', StatView.as_view(), name='stat'),
]
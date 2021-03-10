from django.urls import path
from django.shortcuts import render
from map.views import MapView, PlacemarkView

urlpatterns = [
    path('', MapView.as_view(), name='map'),
    path('placemarks/', PlacemarkView.as_view(), name='placemarks')
]
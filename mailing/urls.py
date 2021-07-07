from django.urls import path
from django.shortcuts import render
from mailing.views import UnsubscribeView


urlpatterns = [
    path('unsubscribe/', UnsubscribeView.as_view(), name='unsubscribe'),

]
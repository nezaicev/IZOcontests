from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from contests import models
from event.models import Event
from event.serializers import EventSerializer

# Create your views here.


class StatView(TemplateView):
    template_name = 'stat/stat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contests'] = (
            {'name': models.Artakiada.objects.first().info.name if models.Artakiada.objects.first() else 0,
             **models.Artakiada.get_stat_data()},
            {'name': models.NRusheva.objects.first().info.name if models.NRusheva.objects.first() else 0,
             **models.NRusheva.get_stat_data()} ,
            {'name': models.VP.objects.first().info.name if models.VP.objects.first() else 0,
             **models.VP.get_stat_data()},
            {'name': models.Mymoskvichi.objects.first().info.name if models.Mymoskvichi.objects.first() else 0,
             **models.Mymoskvichi.get_stat_data()},)
        return context

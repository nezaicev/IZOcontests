from rest_framework import filters
import django_filters
from frontend.apps import  StandardResultsSetPagination
from django.shortcuts import render

from contests.models import Archive, NominationVP, DirectionVP, ThemeART,NominationMYMSK, \
    ThemeRUSH, Artakiada
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from contests.serializers import ArchiveSerializer, NominationVPSerializer, \
    DirectionVPSerializer, ThemeNRushevaSerializer, ThemeArtakiadaSerializer, NominationMymoskvichiSerializer


def index(request):
    return render(request, 'frontend/index.html')


class ArchiveAPIView(ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['contest_name', 'status', 'direction', 'publish',
                     'nomination', 'theme']
    ordering_fields = ['rating']
    ordering = ['-rating']
    pagination_class = StandardResultsSetPagination


class NominationVPAPIView(ListAPIView):
    queryset = NominationVP.objects.all()
    serializer_class = NominationVPSerializer


class NominationMymoskvichiAPIView(ListAPIView):
    queryset = NominationMYMSK.objects.all()
    serializer_class = NominationMymoskvichiSerializer


class ThemeArtakiadaAPIView(ListAPIView):
    queryset = ThemeART.objects.all()
    serializer_class = ThemeArtakiadaSerializer


class ThemeNRushevaAPIView(ListAPIView):
    queryset = ThemeRUSH.objects.all()
    serializer_class = ThemeNRushevaSerializer


class DirectionVPAPIView(ListAPIView):
    queryset = DirectionVP.objects.all()
    serializer_class = DirectionVPSerializer

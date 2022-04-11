import django_filters
from django.shortcuts import render
from contests.models import Archive, NominationVP, DirectionVP
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from contests.serializers import ArchiveSerializer, NominationVPSerializer, \
    DirectionVPSerializer


def index(request):
    return render(request, 'frontend/index.html')


class ArchiveAPIView(ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['contest_name', 'status', 'direction','publish','nomination']


class NominationVP_API_View(ListAPIView):
    queryset = NominationVP.objects.all()
    serializer_class = NominationVPSerializer


class DirectionVP_API_View(ListAPIView):
    queryset = DirectionVP.objects.all()
    serializer_class = DirectionVPSerializer

from rest_framework import filters
import django_filters
from frontend.apps import StandardResultsSetPagination
from django.shortcuts import render

from contests.models import Archive, NominationVP, DirectionVP, ThemeART, \
    NominationMYMSK, \
    ThemeRUSH, CreativeTack
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from contests.serializers import ArchiveSerializer, NominationVPSerializer, \
    DirectionVPSerializer, ThemeNRushevaSerializer, ThemeArtakiadaSerializer, \
    NominationMymoskvichiSerializer


def index(request):
    return render(request, 'frontend/index.html')


class ArchiveAPIView(ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['contest_name', 'status', 'direction', 'publish',
                     'nomination', 'theme', 'year_contest']
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


class YearContestAPIView(APIView):

    def get(self, request):
        contest_name = request.query_params.get('contest_name')
        years = set(
            Archive.objects.filter(contest_name=contest_name).values_list(
                'year_contest', flat=True))
        years = list(years)
        years.sort(reverse=True)
        return Response(years)


class NominationContestAPIView(APIView):

    def get(self, request):
        contest_name = request.query_params.get('contest_name')
        year = request.query_params.get('year_contest')
        nominations = set(
            Archive.objects.filter(contest_name=contest_name,
                                   year_contest=year).values_list(
                'nomination', flat=True))
        nominations = list(nominations)
        nominations.sort(reverse=True)
        return Response(nominations)


class ThemeContestAPIView(APIView):

    def get(self, request):
        contest_name = request.query_params.get('contest_name')
        year = request.query_params.get('year_contest')
        themes = set(
            Archive.objects.filter(contest_name=contest_name,
                                   year_contest=year).values_list(
                'theme', flat=True))
        themes = list(themes)
        themes.sort(reverse=True)
        return Response(themes)


class CreativeTackAPIView(APIView):

    def get(self, request):
        contest_name = request.query_params.get('contest_name')
        year = request.query_params.get('year_contest')
        theme = request.query_params.get('theme')
        content = set(
            CreativeTack.objects.filter(contest_name=contest_name,
                                        year_contest=year,
                                        theme=theme).values_list(
                'content', flat=True))

        return Response(content)

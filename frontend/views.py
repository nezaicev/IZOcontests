from django.http import Http404
from rest_framework import filters, status
import django_filters

from rest_framework.permissions import BasePermission, SAFE_METHODS

from exposition.models import Exposition
from exposition.serializers import ExpositionSerializer, \
    ExpositionListSerializer
from frontend.apps import StandardResultsSetPagination
from django.shortcuts import render
from contests.models import Archive, NominationVP, DirectionVP, ThemeART, \
    NominationMYMSK, \
    ThemeRUSH, CreativeTack
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from rest_framework.response import Response
from contests.serializers import ArchiveSerializer, NominationVPSerializer, \
    DirectionVPSerializer, ThemeNRushevaSerializer, ThemeArtakiadaSerializer, \
    NominationMymoskvichiSerializer
from event.models import Event, ParticipantEvent
from event.serializers import EventSerializer, ParticipantEventSerializers
from content.models import Page
from content.serializers import PageSerializer
from contests.tasks import send_mail_for_subscribers


class AuthView(APIView):
    """
    frontend/api/auth/
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        content = {
            'id': request.user.id,
            'user': str(request.user),
            'auth': request.user.is_authenticated,
        }
        return Response(content)


def index(request):
    return render(request, 'frontend/index.html')


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            if request.user.is_superuser:
                return True
            else:
                return False
        else:
            return True


class SelfOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            if str(request.user.id) == request.query_params.get('participant'):
                return True
            else:
                return False
        else:
            return True


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class ArchiveAPIView(ModelViewSet):
    authentication_classes = [CsrfExemptSessionAuthentication,
                              BasicAuthentication]
    permission_classes = [AdminOnly]
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
            Archive.objects.filter(theme__gt='', theme__isnull=False,
                                   contest_name=contest_name,
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


class EventListView(APIView):

    def get(self, request, format=None):
        events = Event.objects.filter(hide=False)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventDetailView(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        events = self.get_object(pk)
        serializer = EventSerializer(events)
        return Response(serializer.data)


class BroadcastListView(APIView):

    def get(self, request, format=None):
        broadcasts = Event.objects.filter(broadcast_url__isnull=False)
        serializer = EventSerializer(broadcasts, many=True)
        return Response(serializer.data)


class BroadcastDetailView(APIView):
    def get_object(self, pk):
        try:
            event = Event.objects.get(pk=pk)
            if event.broadcast_url:
                return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        broadcast = self.get_object(pk)
        serializer = EventSerializer(broadcast)
        return Response(serializer.data)


class ParticipantEventDetailView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication,
                              BasicAuthentication]
    permission_classes = [SelfOnly]

    def get_object(self, participant, event):
        try:
            return ParticipantEvent.objects.get(event__id=event,
                                                participant__id=participant,

                                                )
        except Event.DoesNotExist:
            raise Http404

    def get(self, request):
        user_id = request.query_params.get('participant')
        event_id = request.query_params.get('event')
        participant_event = self.get_object(user_id, event_id)
        serializer = ParticipantEventSerializers(participant_event)
        return Response(serializer.data)

    def put(self, request, format='None'):
        """
        {
        event:id,
        participant:id
        }
        """
        serializer = ParticipantEventSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            event = Event.objects.get(id=request.data['event'])
            if event.send_letter:
                send_mail_for_subscribers.delay([request.user.email, ],
                                                event.name, event.letter)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user_id = request.query_params.get('participant')
        event_id = request.query_params.get('event')
        participant_event = self.get_object(user_id, event_id)
        participant_event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ParticipantEventListView(APIView):

    def get_list_objects(self, user_id):
        participant_event_list = ParticipantEvent.objects.filter(
            participant__id=user_id)
        return participant_event_list

    def get(self, request):
        user_id = request.query_params.get('participant')
        participant_event = self.get_list_objects(user_id)
        serializer = ParticipantEventSerializers(participant_event, many=True)
        return Response(serializer.data)


class ExpositionListAPIView(APIView):

    def get(self, request):
        is_archive = request.query_params.get('is_archive')
        if is_archive is None:
            expositions = Exposition.objects.filter(publicate=True)
        else:
            expositions = Exposition.objects.filter(archive=is_archive, publicate=True)
        serializer = ExpositionListSerializer(expositions, many=True)
        return Response(serializer.data)


class ExpositionDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Exposition.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        exposition = self.get_object(pk)
        serializer = ExpositionSerializer(exposition)
        return Response(serializer.data)


class PageDetailAPIView(APIView):
    def get_object(self, slug):
        try:
            return Page.objects.get(slug=slug)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        page = self.get_object(slug)
        serializer = PageSerializer(page)
        return Response(serializer.data)
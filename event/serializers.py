import pytz
from rest_framework import serializers
from event.models import Event, ParticipantEvent


class EventSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(
        default_timezone=pytz.timezone('Europe/Moscow'))

    class Meta:
        model = Event
        fields = ('id','name', 'logo', 'start_date', 'message', 'broadcast_url','reset_registration')


class ParticipantEventSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParticipantEvent
        fields = ('event', 'participant')
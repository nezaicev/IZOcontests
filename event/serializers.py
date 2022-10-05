from rest_framework import serializers
from event.models import Event, ParticipantEvent


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id','name', 'logo', 'start_date', 'message', 'broadcast_url')


class ParticipantEventSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParticipantEvent
        fields = ('event', 'participant')
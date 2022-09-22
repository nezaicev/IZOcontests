from rest_framework import serializers
from event.models import Event, ParticipantEvent


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'logo','start_date', 'message')


class ParticipantEventSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParticipantEvent
        fields = ('reg_number','event', 'participant')
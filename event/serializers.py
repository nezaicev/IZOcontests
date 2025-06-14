import pytz
from rest_framework import serializers
from event.models import Event, ParticipantEvent
from utils import extract_rutube_id, get_rutube_thumbnail


class EventSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(
        default_timezone=pytz.timezone('Europe/Moscow'))

    class Meta:
        model = Event
        fields = ('id','name', 'logo', 'start_date', 'message', 'broadcast_url','reset_registration')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        link = data.get("broadcast_url", "")
        if link:
            if "rutube" in link:
                video_id = extract_rutube_id(link)
                if video_id:
                    poster_url = get_rutube_thumbnail(video_id)
                    if poster_url:
                        data["poster"] = poster_url  # Добавляем в вывод

        return data



class ParticipantEventSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParticipantEvent
        fields = ('event', 'participant')
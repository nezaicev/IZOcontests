from django.contrib import admin
from event.models import ParticipantEvent, Event


class ParticipantEventAdmin(admin.ModelAdmin):
    model = ParticipantEvent
    list_display = ['reg_number','get_fio_participant', 'event', 'certificate', 'status']
    exclude = ['reg_number']

    def get_fio_participant(self, obj):
        return '{} - {}'.format(obj.participant.fio, obj.participant.email )

    get_fio_participant.short_description = 'Участник'


admin.site.register(Event)
admin.site.register(ParticipantEvent, ParticipantEventAdmin)

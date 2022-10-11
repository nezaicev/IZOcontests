from django.contrib import admin
from django_changelist_toolbar_admin.admin import DjangoChangelistToolbarAdmin
from django_simple_export_admin.admin import DjangoSimpleExportAdmin

from event.models import ParticipantEvent, Event


class EventAdmin(admin.ModelAdmin):
    model = Event
    readonly_fields = ['event_url']


class ParticipantEventAdmin(DjangoSimpleExportAdmin, admin.ModelAdmin):
    model = ParticipantEvent
    list_display = ['reg_number', 'get_fio_participant', 'event',
                    'certificate']
    list_filter=['event',]
    exclude = ['reg_number',]

    django_simple_export_admin_exports = {
        "filtered-books": {
            "label": "Выгрузить список",
            "icon": "fas fa-book",
            "fields": [
                {"field": "reg_number", "label": "Регистрационный номер",
                 },
                {"field": "event__name", "label": "Мероприятие"},

                {"field": "participant__fio", "label": "ФИО"},
                {"field": "participant__school", "label": "Организация"},
                {"field": "participant__city", "label": "Город"},
                {"field": "participant__region__name", "label": "Регион"},
            ],
            "export-filtered": True,
            "permissions": [
                "django_simple_export_admin_example.export_filtered_books"],
        }
    }

    def get_fio_participant(self, obj):
        return '{} - {}'.format(obj.participant.fio, obj.participant.email)

    get_fio_participant.short_description = 'Участник'


admin.site.register(Event, EventAdmin)
admin.site.register(ParticipantEvent, ParticipantEventAdmin)

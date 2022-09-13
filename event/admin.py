from django.contrib import admin
from django_changelist_toolbar_admin.admin import DjangoChangelistToolbarAdmin
from django_simple_export_admin.admin import DjangoSimpleExportAdmin

from event.models import ParticipantEvent, Event


class ParticipantEventAdmin(DjangoSimpleExportAdmin, admin.ModelAdmin):
    model = ParticipantEvent
    list_display = ['reg_number', 'get_fio_participant', 'event',
                    'certificate']
    exclude = ['reg_number']

    django_simple_export_admin_exports = {
        "filtered-books": {
            "label": "Выгрузить список",
            "icon": "fas fa-book",
            "fields": [
                {"field": "reg_number", "label": "Number",
                 },
                {"field": "event__name", "label": "Event"},

                {"field": "participant__fio", "label":"FIO"},
            ],
            "export-filtered": True,
            "permissions": [
                "django_simple_export_admin_example.export_filtered_books"],
        }
    }

    def get_fio_participant(self, obj):
        return '{} - {}'.format(obj.participant.fio, obj.participant.email)

    get_fio_participant.short_description = 'Участник'


admin.site.register(Event)
admin.site.register(ParticipantEvent, ParticipantEventAdmin)
